import os

from tree.branch.branch import Branch

from tree.file.index import index as index_file
from tree.file.find import find as find_file
from tree.file.file import File


def index(branch: Branch, root: str):
    for sub_branch in branch.branches.values():
        if not index(sub_branch, root):
            return False

    for header in branch.headers.values():
        if not index_file(header, root):
            return False

    for source in branch.sources.values():
        if not index_file(source, root):
            return False

    return True
