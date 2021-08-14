from tree.branch.source.source import Source

def print_(source: Source, leader: str = ''):
    print(leader, source.name, end='')

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
