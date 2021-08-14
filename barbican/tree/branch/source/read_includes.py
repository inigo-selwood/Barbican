import re


def read_includes(file: str):

    # Create a pattern matching the include pattern
    pattern = re.compile('#include[ \t]*".+"')

    # Match all instances of the pattern in the file, extracting the filename
    includes = []
    for index, line in enumerate(open(file)):
        for match in re.finditer(pattern, line):
            substring = match.group()
            start = substring.find('"') + 1
            includes.append(substring[start:-1])

    return includes
