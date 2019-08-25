"""Version Command"""

import sys

import click

from rabbot.__version__ import __version__


class Version:
    """Contains all version details."""
    def __init__(self, version=__version__):
        super(Version, self).__init__()
        self._version = version

    def about(self):
        """Returns a dict containing the version details"""
        about = {
            '__version__': self._version
        }

        return about


@click.command(
    'version',
    help='Shows the current version of the CLI and exits.',
    short_help='Shows the current version of the CLI.'
)
@click.help_option('-h', '--help')
def cli():
    """Entry point for command."""
    version = Version()
    click.echo(
        '{0} {1}'.format('Rabbot', version.about().get('__version__'))
    )
    sys.exit(0)
