import os


def get_base(base: str = os.getcwd()):

    """ Finds the parent of the root directory (if one exists)

    Checks parent directories until either the filesys. root (`/`)) is reached,
    or a `.barbican` folder is tracked down

    Arguments
    ---------
    base: str
        the directory in which to start looking

    Returns
    -------
    base: str
        the name of the root parent folder, or None if one couldn't be found
    """

    files = os.listdir(base)

    # Find the first instance of a .barbican folder, until the root is reached
    while '.barbican' not in files:
        if base == '/':
            return None

        base = os.path.dirname(base)

    return base
