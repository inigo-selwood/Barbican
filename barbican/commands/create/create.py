import click
import os

from commands.utilities.context_exists import context_exists


@click.command('create', short_help='create a Barbican context')
@click.argument('base',
        required=False,
        type=click.Path(exists=True, file_okay=False, resolve_path=True))
def command(base: str = None):

    # Use the current working directory as a base if none has been given
    if not base:
        base = os.getcwd()

    # Check a context doesn't already exist at the base given
    if context_exists(base):
        print('barbican: context already exists')
        return 1

    # Create the context
    path = os.path.join(base, '.barbican')
    os.mkdir(path)
    print('barbican: context created')
    return 0
