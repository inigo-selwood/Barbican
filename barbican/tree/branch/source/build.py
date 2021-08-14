import os

from tree.branch.source.source import Source
from tree.branch.source.hash import hash as hash_source
from tree.branch.source.read_includes import read_includes

def build(path: str, file_name: str):
    source = Source()

    absolute_path = os.path.join(path, file_name)
    source.hash = hash_source(absolute_path)
    source.includes = read_includes(absolute_path)

    return source
