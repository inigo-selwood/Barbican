import os


def context_exists(base: str):

    path = os.path.join(base, '.barbican')
    if os.path.isdir(path):
        return True
    elif not base or base == '/':
        return False

    new_base = os.path.dirname(base)
    return context_exists(new_base)
