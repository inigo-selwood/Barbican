from tree.branch.source.source import Source
from tree.status.status import Status


def print_(source: Source, leader: str = '', starter: str = ''):

    """ Prints a source object

    Uses leader, starter arguments to properly indent and format the source and
    any other fields (dependencies etc.). 

    Arguments
    ---------
    source: Source
        the source object to print
    leader: str
        text to print for subsequent fields
    starter:
        text to print before the source name
    """

    # Print tree structure leader, and an optional hint that indicates status
    print(starter, end='')
    if source.status == Status.ADDED:
        print('+ ', end='')
    elif source.status == Status.REMOVED:
        print('- ', end='')
    elif source.status == Status.ALTERED:
        print('* ', end='')

    # Print name, and any included files
    # print(f'\033[31m*\033[0m', end='')
    print(source.name)
