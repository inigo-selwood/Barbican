from tree.branch.save import save as save_branch
from tree.get_root import get_root
from tree.branch.branch import Branch


def save(root: Branch, base: str = get_root()):

    """ Saves a tree

    Arguments
    ---------
    root: Branch
        the root of the tree to save
    base: str
        the directory in which to save the tree
    """

    save_branch(root, base)
