from tree.branch.branch import Branch
from tree.branch.compare import compare as compare_branch


def compare(old_tree: Branch, new_tree: Branch) -> Branch:
    return compare_branch(old_tree, new_tree)
