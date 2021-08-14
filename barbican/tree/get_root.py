import os

from tree.get_base import get_base


def get_root():
    base = get_base()
    if not base:
        return None

    return os.path.join(base, '.barbican')
