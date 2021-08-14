class Source:

    def __init__(self):
        self.hash = ''
        self.includes = []

    def __str__(self):
        if not self.includes:
            return ''

        print(': ', end = '')
        include_count = len(self.includes)
        for index in range(include_count):
            include = self.includes[index]
            print(f'{include}', end=', ' if (index + 1) < include_count else '')

        return ''
