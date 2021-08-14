import hashlib

from tree.branch.branch import Branch

def hash(branch: Branch):
    hashes = []
    for branch_ in branch.branches:
        hashes.append(branch_.hash)
    for source in branch.sources:
        hashes.append(source.hash)
    hashes = sorted(hashes)

    branch_hash = hashlib.shake_256()
    for hash in sorted(hashes):
        branch_hash.update(hash.encode())

    return branch_hash.hexdigest(8)
