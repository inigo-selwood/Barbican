import os


def get_base(base: str = os.getcwd()):
    files = os.listdir(base)

    # Find the first instance of a .barbican folder, until the root is reached 
    while '.barbican' not in files:
        if base == '/':
            return None

        base = os.path.dirname(base)

    return base
