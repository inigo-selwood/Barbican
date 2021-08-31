import click
import os

from tree.branch.display import display as display_tree
from tree.branch.load import load as load_tree

from commands.utilities.find_context import find_context


@click.command('load', short_help='load a tree')
def command():

    # Check a context exists
    base = find_context(os.getcwd())
    if not base:
        print('barbican: no context found')
        return 1

    tree = load_tree(base, '.')
    display_tree(tree)
