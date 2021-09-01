import os

from tree.branch.branch import Branch


def get_build(branch: Branch):
    if not branch.parent:
        return os.path.join('.barbican', branch.hash)
    else:
        parent_hash = get_build(branch.parent)
        return os.path.join(parent_hash, branch.hash)
