from tree.branch.build import build as build_branch
from tree.get_base import get_base


def build(path: str = get_base()):

    """ Build a virtual tree representation of a project

    Arguments
    ---------
    path: str
        the path to start building from (should be the project root)

    Returns
    -------
    tree: Branch
        the tree constructed

    Raises
    ------
    exception: Exception
        if no build folder was found at the path specified
    """

    # Check a path was found
    if not path:
        raise Exception("no root folder found, use 'barbican create'")

    return build_branch(path, '.', 0)
