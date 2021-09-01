import os

from tree.branch.branch import Branch

from tree.file.index import index as index_file
from tree.file.find import find as find_file
from tree.file.file import File

from tree.branch.route.get_build import get_build as get_build_route


def index(branch: Branch, root: str):

    build_base = get_build_route(branch)
    build_path = os.path.join(root, build_base)
    if not os.path.isdir(build_path):
        os.mkdir(build_path)

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
