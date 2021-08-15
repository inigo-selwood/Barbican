import os

from tree.branch.source.hash import hash as hash_source
from tree.branch.source.read_includes import read_includes
from tree.branch.source.source import Source


def build(path: str, file_name: str) -> Source:

    """ Build a source object from a C source or header file

    Arguments
    ---------
    path: str
        the file's directory's absolute path
    file_name: str
        the name of the file, including its extension

    Returns
    -------
    source: Source
        the source object loaded
    """

    # Create a source object
    source = Source()
    source.name = file_name

    # Infer its hash and inclusions
    absolute_path = os.path.join(path, file_name)
    source.hash = hash_source(absolute_path)
    source.includes = read_includes(absolute_path)

    return source
