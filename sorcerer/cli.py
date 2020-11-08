import click
import json
import os
from .generator import Generator


@click.command()
@click.option("--git", "-g", required=True)
def cli(git):
    """
    Entry point for the cli. Looks for config file in
    current directory.

    :param git: User's github username
    """
    if os.path.exists("./config.json"):
        with open("./config.json") as file:
            try:
                config = json.load(file)
            except Exception as error:
                print("Error: {}".format(error))
                exit()
    else:
        click.secho("Config file not found.", fg="red")
        exit()

    Generator(git, config).generate()


if __name__ == "__main__":
    cli()
