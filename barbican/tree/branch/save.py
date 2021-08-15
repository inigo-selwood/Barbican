import os
import yaml

from tree.branch.branch import Branch


def save(branch: Branch, path: str):

    """ Saves a branch, encoded in yaml

    Serializes the persistent fields of a branch (ignoring things like its
    build status etc.). For example:

    ``` yaml
    name: program
    path: /some-path/another-folder/program
    branches:
      a_branch: 643be4cf851ce452
    headers: {}
    sources:
      thing.hpp:
        hash: 24c898579fb88616
        includes:
        - stuff/stuff.hpp
    ```

    Arguments
    ---------
    branch: Branch
        branch to encode
    path: str
        absolute path of filename to save branch to
    """

    # Check the directory exists
    if not os.path.exists(path):
        os.mkdir(path)

    # Serialize sources
    sources = {}
    for name, source in branch.sources.items():
        sources[name] = {
            'hash': source.hash,
            'includes': source.includes
        }

    # Serialize header files
    headers = {}
    for name, header in branch.headers.items():
        headers[name] = {
            'hash': header.hash,
            'includes': header.includes
        }

    # Serialize branches
    branches = {}
    for name, branch_ in branch.branches.items():
        branches[name] = branch_.hash

    for name, branch_ in branch.branches.items():
        new_path = os.path.join(path, name)
        save(branch_, new_path)

    # Put the packet together, encode it as yaml, and write it to file
    branch_data = {
        'name': branch.name,
        'path': branch.path,
        'branches': branches,
        'headers': headers,
        'sources': sources
    }

    absolute_path = os.path.join(path, '.branch')
    with open(absolute_path, 'w') as branch_file:
        yaml.dump(branch_data, branch_file)
