import re


def read_includes(path: str):

    includes = []
    with open(path, 'r') as file:

        pattern = re.compile(r'#include[ \t]*\"[^\"]+\"')
        for line in file:

            # Pull the name of the included file out of the match
            matches = re.findall(pattern, line)
            for match in matches:
                start = match.find('\"') + 1
                include = match[start:-1]
                includes.append(include)

    return includes
