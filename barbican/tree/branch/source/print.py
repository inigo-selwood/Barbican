from tree.branch.source.source import Source
from tree.status.status import Status

def print_(source: Source, leader: str = ''):
    print(leader, end='')

    if source.status == Status.ADDED:
        print('+ ', end='')
    elif source.status == Status.REMOVED:
        print('- ', end='')
    elif source.status == Status.ALTERED:
        print('* ', end='')

    print(source.name, end='')

    # if source.dirty:
    #     print(f'\033[31m*\033[0m', end='')

    if source.includes:
        print(': ', end='')

    index = 0
    for include in source.includes:
        print(include, end='')
        if (index + 1) < len(source.includes):
            print(', ', end='')
        index += 1

    print('')
