import click
import json
import os
from .generator import Generator


@click.command()
@click.option('--git', prompt='Github link to repository')
@click.option('--local_path', prompt='Local path to repository')
def cli(git, local_path):
    # Load json config
    CONFIG = {}
    if os.path.exists('{}/config.json'.format(local_path)):
        with open('{}/config.json'.format(local_path)) as f:
            try:
                CONFIG = json.load(f)
            except Exception as e:
                print(e)
                exit()
    else:
        print("Config file not found.")
        exit()

    generator = Generator(local_path, git, CONFIG)
    generator.generate()


if __name__ == '__main__':
    cli()
