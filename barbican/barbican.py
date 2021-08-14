import argparse

from tree.build import build as build_tree
from tree.load import load as load_tree
from tree.save import save as save_tree

parser = argparse.ArgumentParser()
parser.add_argument('command')
args = parser.parse_args()

if args.command == 'build':
    tree = build_tree()
    save_tree(tree)
    print(tree)
elif args.command == 'load':
    tree = load_tree()
    print(tree)
else:
    raise Exception(f"unrecognized command: '{args.command}'")
