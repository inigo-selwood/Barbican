import os

from tree.branch.branch import Branch


def get_source(branch: Branch):
    if not branch.parent:
        return branch.name
    else:
        parent_hash = get_source(branch.parent)
        return os.path.join(parent_hash, branch.name)
