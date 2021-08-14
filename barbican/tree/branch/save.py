import os
import yaml

from tree.branch.branch import Branch


def save(branch: Branch, path: str):

    if not os.path.exists(path):
        os.mkdir(path)

    sources = {}
    for name, source in branch.sources.items():
        sources[name] = source.hash

    branches = {}
    for name, branch_ in branch.branches.items():
        branches[name] = branch_.hash

    for name, branch_ in branch.branches.items():
        new_path = os.path.join(path, name)
        save(branch_, new_path)

    branch_data = {
        'path': branch.path,
        'branches': branches,
        'sources': sources
    }

    absolute_path = os.path.join(path, '.branch')
    with open(absolute_path, 'w') as branch_file:
        yaml.dump(branch_data, branch_file)
