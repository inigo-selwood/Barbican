import os

from tree.branch.load import load as load_branch
from tree.get_root import get_root

def load(path: str = get_root()):
    return load_branch(path, 0)
