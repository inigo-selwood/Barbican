import os
import yaml

from tree.branch.source.source import Source
from tree.branch.branch import Branch

def load(path: str, depth: int):
    branch_file_name = os.path.join(path, '.branch')
    branch_file = open(branch_file_name, 'r')

    values = yaml.safe_load(branch_file)

    branch = Branch()
    branch.path = values['path']
    branch.depth = depth

    for name, source_ in values['sources'].items():
        source = Source()
        source.hash = source_['hash']
        source.includes = source_['includes']

        branch.sources[name] = source

    for name, hash in values['branches'].items():
        absolute_path = os.path.join(path, name)
        branch_ = load(absolute_path, depth + 1)

        branch_.hash = hash
        branch.branches[name] = branch_

    branch_file.close()
    return branch
