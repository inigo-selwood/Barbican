import click
import os

from commands.build import build
from commands.create import create
from commands.load import load
from commands.index import index


@click.group()
def barbican():
    pass


if __name__ == '__main__':
    barbican.add_command(build.command)
    barbican.add_command(create.command)
    barbican.add_command(load.command)
    barbican.add_command(index.command)

    barbican()
