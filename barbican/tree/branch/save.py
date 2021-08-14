import os
import yaml

from tree.branch.branch import Branch


def save(branch: Branch, path: str):

    if not os.path.exists(path):
        os.mkdir(path)

    sources = {}
    for source in branch.sources:
        sources[f'{source.name}{source.extension}'] = source.hash

    branches = {}
    for branch_ in branch.branches:
        branches[branch_.name] = branch_.hash

    for branch_ in branch.branches:
        new_path = os.path.join(path, branch_.name)
        save(branch_, new_path)

    branch_data = {
        'name': branch.name,
        'path': branch.path,
        'branches': branches,
        'sources': sources
    }

    absolute_path = os.path.join(path, '.branch')
    with open(absolute_path, 'w') as branch_file:
        yaml.dump(branch_data, branch_file)
