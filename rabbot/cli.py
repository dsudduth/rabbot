"""Entry point for CLI."""

import os
import click
import logging

from pathlib import Path

CMD_FOLDER = str(Path(os.path.dirname(__file__), "commands").resolve())
CMD_PREFIX = "cmd_"

logger = logging.getLogger(__name__)


class RabbotCLI(click.MultiCommand):
    """
    Multi-command class for Rabbot. Handles gathering subcommands.
    """

    def list_commands(self, ctx):
        """
        Creates a list of commands by reading in the files in the CLI's
        'commands' directory.

        :param ctx:
        :return: List of strings representing the names of commands
        """
        commands = []
        for filename in os.listdir(CMD_FOLDER):
            if filename.endswith(".py") and filename.startswith(CMD_PREFIX):
                commands.append(filename[4:-3])
        commands.sort()
        return commands

    def get_command(self, ctx, name):
        """
        Modifies Click's subcommands by importing each 'cmd_' file as a
        module, adding them to the UI, and making them available
        to the caller.

        :param ctx:
        :param name: name of the command
        :return: Returns the modified cli object containing the available cmds.
        """

        try:
            cmd_base = f"rabbot.commands.{CMD_PREFIX}"
            mod = __import__(cmd_base + name, None, None, ["cli"])
            if hasattr(mod, "subcommand"):
                return getattr(mod, "subcommand")
        except ImportError:
            return
        return mod.cli


@click.command(
    cls=RabbotCLI,
    epilog='See "COMMAND -h" to read about a specific subcommand',
    short_help="%(prog)s [-h] COMMAND [args]",
)
@click.help_option("-h", "--help")
def cli():
    """
    Rabbot is a utility for testing connections to RabbitMQ servers.
    """
    pass


if __name__ == "__main__":
    cli()
