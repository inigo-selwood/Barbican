import click
import os

from tree.branch.load import load as load_tree
from tree.branch.index import index as index_tree
from tree.branch.display import display as display_tree
from tree.file.compile import compile as compile_target
from tree.file.find import find as find_file

from commands.utilities.find_context import find_context


@click.command('build', short_help='build the build tree of a target')
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

    # display_tree(tree)

    target_route = os.path.relpath(target, base)
    target_file = find_file(target_route, tree)
    if not target_file:
        print("barbican: couldn't find 'target_route'")
        return 1

    if not compile_target(target_file, base):
        return 1

    return 0
