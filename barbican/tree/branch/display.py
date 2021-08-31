from tree.branch.branch import Branch

from tree.file.display import display as display_file


def get_starter(index: int, count: int):
    if (index + 1) < count:
        return '├─ '
    else:
        return '╰─ '


def display(branch: Branch, leader: str = '', final: bool = True, root: bool = True):
    starter = '╰─ ' if final else '├─ '
    new_leader = '' if root else f'{leader}│  '

    if root:
        print(branch.name)
    else:
        print(leader, starter, branch.name, sep='')

    index = 0
    count = len(branch.headers) + len(branch.sources) + len(branch.branches)
    for branch_ in branch.branches.values():
        final = (index + 1) == count
        display(branch_, new_leader, final, root=False)
        index += 1

    for header in branch.headers.values():
        final = (index + 1) == count
        display_file(header, new_leader, final)
        index += 1

    for source in branch.sources.values():
        final = (index + 1) == count
        display_file(source, new_leader, final)
        index += 1
