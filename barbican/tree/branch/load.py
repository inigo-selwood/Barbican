import os
import yaml

from typing import Dict

from tree.branch.source.source import Source
from tree.branch.branch import Branch

def _load_files(values: Dict):

    # Create a source object for each entry in the values dict.
    result = {}
    for name, file in values.items():
        source = Source()
        source.name = name
        source.hash = file['hash']
        source.includes = file['includes']

        result[name] = source

    return result


def load(path: str, depth: int):

    # Open the branch file specified
    branch_file_name = os.path.join(path, '.branch')
    branch_file = open(branch_file_name, 'r')

    # Load its values (yaml encoded)
    values = yaml.safe_load(branch_file)

    # Create a new branch
    branch = Branch()
    branch.path = values['path']
    branch.name = values['name']
    branch.depth = depth

    # Load sources and headers
    branch.sources = _load_files(values['sources'])
    branch.headers = _load_files(values['headers'])

    # Load branches
    for name, hash in values['branches'].items():
        absolute_path = os.path.join(path, name)
        branch_ = load(absolute_path, depth + 1)

        branch_.hash = hash
        branch.branches[name] = branch_

    branch_file.close()
    return branch
