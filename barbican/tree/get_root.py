import os

from tree.get_base import get_base


def get_root():

    """ Finds the root directory (if one exists)

    Checks parent directories until either the filesys. root (`/`)) is reached,
    or a `.barbican` folder is tracked down

    Arguments
    ---------
    base: str
        the directory in which to start looking

    Returns
    -------
    base: str
        the name of the root folder, or None if one couldn't be found
    """

    base = get_base()
    if not base:
        return None

    return os.path.join(base, '.barbican')
