from typing import Dict

from tree.branch.branch import Branch
from tree.status.status import Status


def _compare_files(old: Dict, new: Dict):

    # Create a union dict. with both old and new files
    files = old.copy()
    files.update(new)

    dirty = False
    result = new.copy()
    for name, file in files.items():
        clean = False

        # Files removed since the last build
        if name not in new:
            file_ = file.copy()
            file_.status = Status.REMOVED
            result[name] = file_

        # Files added since the last build
        elif name not in old:
            result[name].status = Status.ADDED

        # Files changed since the last build
        elif old[name].hash != new[name].hash:
            result[name].status = Status.ALTERED

        # Files which haven't been changed
        else:
            result[name].status = Status.UNCHANGED
            clean = True

        # Quite proud of how this one reads
        dirty = dirty or not clean

    return dirty, result


def _compare_branches(old: Dict, new: Dict):

    # Create a union dict. with both old and new branches
    branches = old.copy()
    branches.update(new)

    # Iterate each branch
    dirty = False
    result = new.copy()
    for name, branch in branches.items():

        clean = False

        # Branches removed since last build
        if name not in new:
            branch_ = branch.copy()
            branch_.status = Status.REMOVED
            result[name] = branch_

        # Branches added since last build
        elif name not in old:
            result[name].status = Status.ADDED

        # Branches whose file(s), subfolder(s) have been altered
        elif old[name].hash != new[name].hash:
            branch_ = compare(old[name], new[name])
            branch_.status = Status.ALTERED
            result[name] = branch_

        # Files which remain unchanged
        else:
            branch_ = compare(old[name], new[name])
            if branch_.status == Status.UNCHANGED:
                clean = True

        # Update the dirty flag
        dirty = dirty or not clean

    return dirty, result


def compare(old: Branch, new: Branch):
    result = new

    # Find which files, branches have changed, and whether those changes make
    # the branch dirty (ie: neccessitate a rebuild)
    headers_dirty, headers = _compare_files(old.headers, new.headers)
    sources_dirty, sources = _compare_files(old.sources, new.sources)
    branches_dirty, branches = _compare_branches(old.branches, new.branches)

    # Assign the newly-compared files, branches to the result
    result.headers = headers
    result.sources = sources
    result.branches = branches

    # Flag the branch as altered if any of its files, branches were dirty
    branch_dirty = headers_dirty or sources_dirty or branches_dirty
    result.status = Status.ALTERED if branch_dirty else Status.UNCHANGED

    return result
