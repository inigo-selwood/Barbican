import hashlib

from tree.branch.branch import Branch


def hash(branch: Branch):

    # Create a list with the hashes of all the branch's files, [sub]branches
    hashes = []
    for branch_ in branch.branches.values():
        hashes.append(branch_.hash)
    for hash in branch.sources:
        hashes.append(hash)
    for hash in branch.headers:
        hashes.append(hash)

    # Hash each branch in turn (sorted in case for whatever reason the arrival
    # order changes)
    hashes = sorted(hashes)
    branch_hash = hashlib.shake_256()
    for hash in sorted(hashes):
        branch_hash.update(hash.encode())

    return branch_hash.hexdigest(8)
