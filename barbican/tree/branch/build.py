import os

from tree.branch.branch import Branch
from tree.branch.source.source import Source
from tree.branch.source.hash import hash as hash_source
from tree.branch.hash import hash as hash_branch
from tree.branch.source.build import build as build_source

def build(path: str, name: str, depth: int):
    files = []
    directories = []
    for name_ in os.listdir(path):
        absolute_path = os.path.join(path, name_)
        if os.path.isdir(absolute_path) and name_ != '.barbican':
            directories.append(name_)
        else:
            files.append(name_)

    branch = Branch()
    branch.path = path
    branch.depth = depth
    branch.name = name

    header_extensions = ['.hpp', '.hh', '.h']
    source_extensions = ['.cpp', '.cc', '.c']
    for file_name in files:
        name, extension = os.path.splitext(file_name)

        if extension in source_extensions:
            branch.sources[file_name] = build_source(path, file_name)
        elif extension in header_extensions:
            branch.headers[file_name] = build_source(path, file_name)

    new_depth = depth + 1
    for directory in directories:
        new_path = os.path.join(path, directory)
        branch.branches[directory] = build(new_path, directory, new_depth)

    branch.hash = hash_branch(branch)

    return branch
