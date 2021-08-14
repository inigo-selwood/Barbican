from tree.branch.source.source import Source

class Branch:

    def __init__(self):
        self.path = ''
        self.hash = ''
        self.branches = {}
        self.sources = {}
        self.depth = 0

    def __str__(self):
        indent = (self.depth * 2) * '  '

        for name, branch in self.branches.items():
            print(indent, end='')
            print(f'\033[37;0;46m{name}\033[0m')
            branch.__str__()

        for name in self.sources:
            print(indent, end='')
            print(name)

        return ''
