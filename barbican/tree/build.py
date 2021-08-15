from tree.branch.build import build as build_branch
from tree.get_base import get_base


def build(path: str = get_base()):

    # Check a path was found
    if not path:
        raise Exception("no root folder found, use 'barbican create'")

    return build_branch(path, '.', 0)
