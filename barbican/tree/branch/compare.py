from typing import Dict

from tree.branch.branch import Branch
from tree.status.status import Status

def _compare_files(old: Dict, new: Dict):
    result = new.copy()

    files = old.copy()
    files.update(new)

    dirty = False
    for name, file in files.items():
        clean = False

        # File removed from the new tree (but present in the old one)
        if name not in new:
            file_ = file.copy()
            file_.status = Status.REMOVED
            result[name] = file_

        # File added to the new tree (isn't in the old one)
        elif name not in old:
            result[name].status = Status.ADDED

        # Check if the file's hash has changed
        elif old[name].hash != new[name].hash:
            result[name].status = Status.ALTERED

        else:
            result[name].status = Status.UNCHANGED
            clean = True

        # Quite proud of how this one reads
        dirty = dirty or not clean

    return dirty, result


def _compare_branches(old: Dict, new: Dict):
    result = new.copy()

    branches = old.copy()
    branches.update(new)

    dirty = False
    for name, branch in branches.items():

        clean = False

        if name not in new:
            branch_ = branch.copy()
            branch_.status = Status.REMOVED
            result[name] = branch_

        elif name not in old:
            result[name].status = Status.ADDED

        elif old[name].hash != new[name].hash:
            branch_ = compare(old[name], new[name])
            branch_.status = Status.ALTERED
            result[name] = branch_

        else:
            branch_ = compare(old[name], new[name])
            if branch_.status == Status.UNCHANGED:
                clean = True

        dirty = dirty or not clean

    return dirty, result



def compare(old: Branch, new: Branch):
    result = new

    headers_dirty, headers = _compare_files(old.headers, new.headers)
    sources_dirty, sources = _compare_files(old.sources, new.sources)
    branches_dirty, branches = _compare_branches(old.branches, new.branches)

    result.headers = headers
    result.sources = sources
    result.branches = branches

    branch_dirty = headers_dirty or sources_dirty or branches_dirty
    result.status = Status.ALTERED if branch_dirty else Status.UNCHANGED

    return result
