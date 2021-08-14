from tree.branch.save import save as save_branch
from tree.get_root import get_root
from tree.branch.branch import Branch
from tree.get_root import get_root


def save(root: Branch, base: str = get_root()):
    save_branch(root, base)
