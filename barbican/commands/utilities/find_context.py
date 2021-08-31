import os


def find_context(base: str = os.getcwd()):

    path = os.path.join(base, '.barbican')
    if os.path.isdir(path):
        return base
    elif not base or base == '/':
        return None

    new_base = os.path.dirname(base)
    return find_context(new_base)
