import argparse

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
else:
    raise Exception(f"unrecognized command: '{args.command}'")
