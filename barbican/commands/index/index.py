import click
import os

from tree.branch.load import load as load_tree
from tree.branch.index import index as index_tree
from tree.branch.display import display as display_tree

from commands.utilities.find_context import find_context


@click.command('index', short_help='index the build tree of a target')
@click.argument('target',
        required=False,
        type=click.Path(exists=True, dir_okay=False, resolve_path=True))
def command(target: str = None):

    base = find_context()
    if not base:
        print("barbican: no context found, use 'barbican create'")
        return 1

    file_name = os.path.basename(target)
    _, extension = os.path.splitext(file_name)

    if extension not in ['.hpp', '.hh', '.h', '.cpp', '.cc', '.c']:
        print('barbican: not a C/C++ header file')
        return 1

    tree = load_tree(base, '.')
    if not index_tree(tree, base):
        return 1

    display_tree(tree)
