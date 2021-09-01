from termcolor import colored as coloured

from tree.file.file import File


def display(file: File, leader: str, final: bool):

    spacer = '   ' if final else '│  '
    starter = '╰─ ' if final else '├─ '

    # name = coloured(file.name, 'green')
    print(leader, starter, file.name, sep='')

    if 'headers' in file.attributes:
        for header in file.attributes['headers']:
            pointer = coloured('→ ', 'red')
            print(leader, spacer, pointer, header, sep='')

    if 'sources' in file.attributes:
        for source in file.attributes['sources']:
            pointer = coloured('← ', 'green')
            print(leader, spacer, pointer, source, sep='')
