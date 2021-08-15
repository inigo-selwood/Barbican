from tree.branch.load import load as load_branch
from tree.get_root import get_root
from tree.branch.branch import Branch


def load(path: str = get_root()) -> Branch:

    """ Loads a tree that's been saved previously

    The whole premise of the build system is to compare the current state of
    the project file system to a previous version, detect changes, and only
    build the files which have been changed (or depend on others which have
    been).

    After a compilation has succeeded, the tree gets saved as a structure of
    hashes -- and this function will read that frozen cache into a new tree for
    comparison later on.

    Arguments
    ---------
    path: str
        the root directory of the project

    Returns
    -------
    tree: Branch
        the tree loaded
    """

    if not path:
        raise Exception("no root folder found, use 'barbican create'")

    return load_branch(path, 0)
