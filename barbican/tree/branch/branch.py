from tree.branch.source.source import Source

class Branch:

    def __init__(self):
        self.name = ''
        self.path = ''
        self.hash = ''
        self.branches = []
        self.sources = []
        self.depth = 0

    def __str__(self):
        indent = (self.depth * 2) * '  '
        print(indent, end='')
        print(f'\033[37;0;46m{self.name}\033[0m')

        for branch in self.branches:
            branch.__str__()

        indent = ((self.depth + 1) * 2) * '  '
        for source in self.sources:
            print(indent, end='')
            print(source)

        return ''
