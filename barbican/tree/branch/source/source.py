class Source:

    def __init__(self):
        self.name = ''
        self.extension = ''
        self.hash = ''

    def __str__(self):
        return f'{self.name}{self.extension}'
