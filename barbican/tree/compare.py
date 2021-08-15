from tree.branch.branch import Branch
from tree.branch.compare import compare as compare_branch


def compare(old_tree: Branch, new_tree: Branch) -> Branch:

    """ Compare the contents of two trees

    Creates a new tree indicating which files have been added, removed, or
    changed

    Arguments
    ---------
    old_tree: Branch
        the tree that's been loaded from a root folder
    new_tree: Branch
        newly built tree

    Returns
    -------
    result: Branch
        tree with changes flagged
    """

    return compare_branch(old_tree, new_tree)
