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
