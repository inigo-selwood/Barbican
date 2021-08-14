import argparse
import os

from tree.build import build as build_tree
from tree.load import load as load_tree
from tree.save import save as save_tree
from tree.compare import compare as compare_tree
from tree.branch.print import print_ as print_tree

parser = argparse.ArgumentParser()
parser.add_argument('command')
args = parser.parse_args()

if args.command == 'build':
    tree = build_tree()
    save_tree(tree)
    print_tree(tree)

elif args.command == 'load':
    tree = load_tree()
    print_tree(tree)

elif args.command == 'compare':
    old_tree = load_tree()
    new_tree = build_tree()
    result = compare_tree(old_tree, new_tree)
    print_tree(result)

elif args.command == 'create':
    os.mkdir(os.path.join(os.getcwd(), '.barbican'))

else:
    raise Exception(f"unrecognized command: '{args.command}'")
