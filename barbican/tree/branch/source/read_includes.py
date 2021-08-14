import re

def read_includes(file: str):
    pattern = re.compile('#include[ \t]*".+"')

    includes = []
    for index, line in enumerate(open(file)):
        for match in re.finditer(pattern, line):
            substring = match.group()
            start = substring.find('"') + 1
            includes.append(substring[start:-1])

    return includes
