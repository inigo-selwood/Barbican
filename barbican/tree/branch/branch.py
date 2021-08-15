from tree.status.status import Status


class Branch:

    def __init__(self):
        self.path = ''
        self.hash = ''
        self.name = ''
        self.branches = {}
        self.sources = {}
        self.headers = {}
        self.status = Status.UNCHANGED
        self.depth = 0
        self.dirty = False
