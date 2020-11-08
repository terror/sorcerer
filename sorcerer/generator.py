import click
import os
from collections import defaultdict
from .constants import sites, languages


class Generator:
    """
    Responsible for generating the markdown tables

    :param git: User's github username
    :param config: User's config file
    """

    def __init__(self, git, config):
        self.git = git
        self.config = config

    def generate(self):
        """
        Generates the markdown tables with
        respect to the user's config file
        """

        # Get all directories in config file
        directories = self.config["Paths"]

        # Github link to the repository
        git_link = "https://github.com/{}/{}/".format(
            self.git, os.path.basename(os.getcwd())
        )

        # Walk through directories
        for directory in directories:
            table, site = defaultdict(list), directory

            try:
                self.create_readme(directory, site)
            except Exception as error:
                print("Error: {}".format(error))

            self.populate_map(directory, table)

            # Build the README table
            with open(os.path.join(directory, "README.md"), "a") as readme:
                for file, file_extensions in table.items():
                    if len(file_extensions) == 1:
                        readme.write(
                            "[{}]({}/{}) | [{}]({})\n".format(
                                file.capitalize(),
                                sites[site.lower()],
                                file,
                                languages[file_extensions[0]],
                                self.git_file_path(
                                    git_link, directory, file +
                                    file_extensions[0]
                                ),
                            )
                        )
                    else:
                        readme.write(
                            "[{}]({}/{}) | ".format(
                                file.capitalize(), sites[site.lower()], file
                            )
                        )

                        for index, extension in enumerate(file_extensions):
                            readme.write(
                                "[{}]({}){} ".format(
                                    languages[extension],
                                    self.git_file_path(
                                        git_link, directory, file + extension
                                    ),
                                    "," if index != len(
                                        file_extensions) - 1 else "\n",
                                )
                            )

                readme.close()

        click.secho("Process finished!", fg="green")

    def create_readme(self, path, site):
        """
        Creates README file for specified path

        :param path: path for the README file
        """
        site = site.capitalize()

        print("[~] Creating README for {}...".format(site))

        with open(os.path.join(path, "README.md"), "w") as readme:
            readme.write(
                "# {}\n| Problem | Languages |\n| ------- | --------- |\n".format(
                    site)
            )

            readme.close()

    def populate_map(self, directory, table):
        """
        Populate map with file : [extensions]

        :param directory: directory to walk through
        :param table: map to populate
        """
        for subdir, dirs, files in os.walk(directory):
            for file in files:
                filename, file_extension = os.path.splitext(file)

                if file_extension not in languages:
                    continue

                table[filename].append(file_extension)

    def git_file_path(self, git_link, directory, file):
        """
        Builds the github file path to a file in the table.
        C++ -> [C++](github/path/to/file)

        :param git_link: link to users Github repo
        :param directory: current directory (site name)
        :param file: solution file
        :return: github file path
        """
        path = git_link + "blob/master/{}/{}".format(directory, file)

        return path
