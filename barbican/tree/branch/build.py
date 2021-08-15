import os

from tree.branch.branch import Branch
from tree.branch.hash import hash as hash_branch
from tree.branch.source.build import build as build_source


def build(path: str, name: str, depth: int):

    """ Build a branch from a directory

    Building (as opposed to loading) examines the current file structure, and
    builds a tree from the files it finds. It's a representation of the current
    up-to-date codebase

    Arguments
    ---------
    path: str
        the parent directory of the branch
    name: str
        the name of the branch's directory
    depth: int
        the branch's parent count, relative to the `.barbican` root

    Returns
    -------
    source: Source
        the source built
    """

    # Read the files, directories in the path specified
    files = []
    directories = []
    for name_ in os.listdir(path):
        absolute_path = os.path.join(path, name_)
        if os.path.isdir(absolute_path) and name_ != '.barbican':
            directories.append(name_)
        else:
            files.append(name_)

    # Create a new branch object
    branch = Branch()
    branch.path = path
    branch.depth = depth
    branch.name = name

    # Handle files
    header_extensions = ['.hpp', '.hh', '.h']
    source_extensions = ['.cpp', '.cc', '.c']
    for file_name in files:
        name, extension = os.path.splitext(file_name)

        # Place source, header files in seperate containers
        if extension in source_extensions:
            branch.sources[file_name] = build_source(path, file_name)
        elif extension in header_extensions:
            branch.headers[file_name] = build_source(path, file_name)

    # Handle directories
    new_depth = depth + 1
    for directory in directories:
        new_path = os.path.join(path, directory)
        branch.branches[directory] = build(new_path, directory, new_depth)

    # Update the branch's hash based on files, branches
    branch.hash = hash_branch(branch)
    return branch
