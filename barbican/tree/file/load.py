import os

from tree.branch.branch import Branch
from tree.file.file import File

from tree.utilities.hash_file import hash_file
from tree.utilities.read_includes import read_includes


def load(root: str, name: str, parent: Branch) -> File:

    path = os.path.join(root, parent.route, name)

    file = File()
    file.name = os.path.basename(path)
    file.parent = parent
    file.hash = hash_file(path)

    return file
