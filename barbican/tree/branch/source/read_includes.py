import re

from typing import List


def read_includes(file: str) -> List[str]:

    """ Read includes from a file

    Uses regex (oh dear) to extract `#include` statements from a given file,
    for example

    `#include "a_header.hpp"`

    Returns a list: `['a_header.hpp']`

    Arguments
    ---------
    file: str
        the absolute path of the file whose includes to read

    Returns
    -------
    includes: List[str]
        the file's includes
    """

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
