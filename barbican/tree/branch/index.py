import os

from tree.branch.branch import Branch

from tree.file.index import index as index_file
from tree.file.find import find as find_file
from tree.file.file import File


def index(branch: Branch, root: str):

    for sub_branch in branch.branches.values():
        index(sub_branch, root)

    for header in branch.headers.values():
        index_file(header, root)
    for source in branch.sources.values():
        index_file(source, root)
