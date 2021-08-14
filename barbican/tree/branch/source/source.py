class Source:

    def __init__(self):
        self.hash = ''
        self.includes = []

    def __str__(self):
        return f'{self.name}{self.extension}'
