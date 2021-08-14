from tree.branch.source.print import print_ as print_source
from tree.branch.branch import Branch

def print_(branch: Branch, leader: str = ''):

    print(branch.name, end='')

    if branch.dirty:
        print(f'\033[31m* \033[0m')
    else:
        print('')

    branch_index = 0
    branch_count = len(branch.branches)
    file_count = len(branch.headers) + len(branch.sources)
    for _, branch_ in sorted(branch.branches.items()):
        extension = ''
        if (branch_index + 1) == branch_count and file_count == 0:
            extension = '    '
            print(f'{leader}└── ', end='')
        else:
            extension = '│   '
            print(f'{leader}├── ', end='')

        print_(branch_, f'{leader}{extension}')
        branch_index += 1

    file_index = 0
    for _, header in sorted(branch.headers.items()):
        extension = ''
        if (file_index + 1) == file_count:
            extension = '└──'
        else:
            extension = '├──'

        print_source(header, f'{leader}{extension}')
        file_index += 1

    for _, source in sorted(branch.sources.items()):
        extension = ''
        if (file_index + 1) == file_count:
            extension = '└──'
        else:
            extension = '├──'

        print_source(source, f'{leader}{extension}')
        file_index += 1

    return ''
