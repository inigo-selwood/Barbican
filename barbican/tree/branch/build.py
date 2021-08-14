import os

from tree.branch.branch import Branch
from tree.branch.source.source import Source
from tree.branch.source.hash import hash as hash_source
from tree.branch.hash import hash as hash_branch

def build(path: str, depth: int):
    files = []
    directories = []
    for name in os.listdir(path):
        absolute_path = os.path.join(path, name)
        if os.path.isdir(absolute_path):
            directories.append(name)
        else:
            files.append(name)

    branch = Branch()
    branch.path = path
    branch.depth = depth

    source_extensions = ['.hpp', '.hh', '.h', '.cpp', '.cc', '.c']
    for file_name in files:
        name, extension = os.path.splitext(file_name)
        if not extension or extension not in source_extensions:
            continue

        source = Source()

        absolute_path = os.path.join(path, file_name)
        source.hash = hash_source(absolute_path)

        branch.sources[file_name] = source

    new_depth = depth + 1
    for directory in directories:
        if directory == '.barbican':
            continue

        new_path = os.path.join(path, directory)
        branch.branches[directory] = build(new_path, new_depth)

    branch.hash = hash_branch(branch)

    return branch
