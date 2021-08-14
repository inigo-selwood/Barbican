import os

from tree.branch.build import build as build_branch
from tree.get_base import get_base


def build(path: str = get_base()):
    return build_branch(path, '.', 0)
