import click
import os
from pathlib import Path
from .constants import sites, languages
from .utils import list_tolower


class Generator:
    def __init__(self, PATH, GIT, CONFIG):
        self.PATH = PATH
        self.GIT = GIT
        self.CONFIG = CONFIG

    def generate(self):
        i, CURR_PROBLEM, CURR_SITE = 0, "", ""
        for subdir, dirs, files in os.walk(self.PATH, topdown=True):
            # Exclude ignored directories
            dirs[:] = self.exclude_dirs(subdir, dirs)

            # Create READMEs
            for d in dirs:
                if d.lower() in list_tolower(self.CONFIG['Paths']):
                    try:
                        self.create_readme(os.path.join(subdir, d))
                    except Exception as err:
                        print("Error trying to create READMEs.", err)

            for file in files:
                if self.check_subdir(subdir):
                    PATH = os.path.join(subdir, file)
                    # Check if at a solution file
                    if os.path.split(os.path.split(PATH)[0])[1].lower() not in list_tolower(self.CONFIG['Paths']):
                        filename, file_extension = os.path.splitext(
                            PATH)
                        problem_name = os.path.split(os.path.split(
                            PATH)[0])[1].lower()
                        file_dir = os.path.dirname(subdir)
                        site_name = os.path.basename(file_dir).lower()
                        path_parts = Path(PATH).parts
                        git_path = self.GIT + "/blob/master/" + \
                            os.path.join(
                                *path_parts[len(path_parts)-path_parts.index(os.path.basename(os.path.normpath(self.PATH)))+1:])

                        if CURR_SITE != site_name:
                            i = 0

                        if site_name not in sites:
                            print("Invalid folder name.\n Exiting...")
                            exit()

                        if CURR_PROBLEM != problem_name:
                            print(
                                "[~] Creating table entry for: {}/{}...".format(site_name, problem_name))
                            readme = open("{}/README.md".format(file_dir), "a")
                            if i > 0:
                                readme.write("\n")
                            readme.write(" [{}]({}/{}) | [{}]({})".format(
                                problem_name.capitalize(), sites[site_name], problem_name, languages[file_extension], git_path))
                        else:
                            print(
                                "[~] Appending to existing table entry for {}/{}".format(site_name, problem_name))
                            readme = open(
                                "{}/README.md".format(file_dir), "a")
                            readme.write(", [{}]({}) ".format(
                                languages[file_extension], git_path).rstrip())

                        CURR_PROBLEM, CURR_SITE = problem_name, site_name
                        i += 1
                        readme.close()

        click.secho("Process finished!", bold=True)

    def exclude_dirs(self, subdir, dirs):
        self.CONFIG['Ignore'], self.CONFIG['Paths'] = list_tolower(
            self.CONFIG['Ignore']), list_tolower(self.CONFIG['Paths'])
        return [d for d in dirs if d.lower() in self.CONFIG['Paths'] and d.lower() not in self.CONFIG['Ignore'] or self.check_subdir(subdir)]

    def check_subdir(self, subdir):
        subdir = subdir.lower()
        for i in list_tolower(self.CONFIG['Paths']):
            if i in subdir:
                return True
        return False

    def create_readme(self, path):
        title = os.path.basename(path)
        print("[~] Creating README for {}...".format(title))
        with open(os.path.join(path, "README.md"), "w") as f:
            f.write("# {}\n".format(title))
            f.write("| Problem | Languages |\n")
            f.write("| ------- | --------- |\n")
            f.close()
