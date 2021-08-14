from tree.branch.source.print import print_ as print_source
from tree.branch.branch import Branch
from tree.status.status import Status

def print_(branch: Branch, leader: str = '', starter: str = ''):

    print(starter, end='')

    if branch.status == Status.ADDED:
        print('+ ', end='')
    elif branch.status == Status.REMOVED:
        print('- ', end='')
    elif branch.status == Status.ALTERED:
        print('* ', end='')

    print(branch.name)

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

    file_index = 0
    for _, header in sorted(branch.headers.items()):
        extension = '├──'
        if (file_index + 1) == file_count:
            extension = '└──'

        print_source(header, f'{leader}{extension}')
        file_index += 1

    for _, source in sorted(branch.sources.items()):
        extension = '├──'
        if (file_index + 1) == file_count:
            extension = '└──'

        print_source(source, f'{leader}{extension}')
        file_index += 1

    return ''
