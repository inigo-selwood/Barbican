from tree.branch.source.source import Source

class Branch:

    def __init__(self):
        self.path = ''
        self.hash = ''
        self.name = ''
        self.branches = {}
        self.sources = {}
        self.headers = {}
        self.depth = 0

    def __str__(self):
        indent = (self.depth * 2) * '  '

        for name, header in self.headers.items():
            print(indent, name, end = '')
            print(header)

        for name, branch in self.branches.items():
            print(indent, end='')
            print(f'\033[37;0;46m{name}\033[0m')
            branch.__str__()

        for name, source in self.sources.items():
            print(indent, name, end = '')
            print(source)

        return ''
