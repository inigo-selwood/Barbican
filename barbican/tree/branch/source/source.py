from tree.status.status import Status


class Source:

    def __init__(self):
        self.hash = ''
        self.name = ''
        self.includes = []
        self.status = Status.UNCHANGED
