from tree.branch.source.print import print_ as print_source
from tree.branch.branch import Branch
from tree.status.status import Status


def print_(branch: Branch, leader: str = '', starter: str = ''):

    # Print the tree-structure starter, and a little hint to show the branch's
    # status
    print(starter, end='')
    if branch.status == Status.ADDED:
        print('+ ', end='')
    elif branch.status == Status.REMOVED:
        print('- ', end='')
    elif branch.status == Status.ALTERED:
        print('* ', end='')

    print(branch.name)

    # Print sub-branches first
    branch_index = 0
    branch_count = len(branch.branches)
    file_count = len(branch.headers) + len(branch.sources)
    for _, branch_ in sorted(branch.branches.items()):
        extension = '│   '
        starter = '├── '
        if (branch_index + 1) == branch_count and file_count == 0:
            extension = '    '
            starter = '└── '

        print_(branch_, f'{leader}{extension}', f'{leader}{starter}')
        branch_index += 1

    # Print header files next
    file_index = 0
    for _, header in sorted(branch.headers.items()):
        starter = '├── '
        extension = '│   '
        if (file_index + 1) == file_count:
            starter = '└── '
            extension = '    '
        print_source(header, f'{leader}{extension}', f'{leader}{starter}')
        file_index += 1

    # Print source files last
    for _, source in sorted(branch.sources.items()):
        starter = '├── '
        extension = '│   '
        if (file_index + 1) == file_count:
            starter = '└── '
            extension = '    '
        print_source(source, f'{leader}{extension}', f'{leader}{starter}')
        file_index += 1

    return ''
