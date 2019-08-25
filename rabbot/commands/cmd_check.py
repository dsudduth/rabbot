"""Version Command"""

import logging
import click
import pika

logger = logging.getLogger(__name__)


@click.command(
    "check",
    help="Checks the connection of a RabbitMQ server.",
    short_help="Check connection.",
)
@click.option(
    "--server",
    "server",
    required=True,
    type=str,
    help="URL of the RabbitMQ server",
)
@click.option(
    "--virtual-host",
    default="/",
    type=str,
    show_default=True,
    help="The virtual host to use",
)
@click.option(
    "--ssl",
    required=False,
    default=False,
    type=bool,
    show_default=True,
    help="Enable SSL",
)
@click.option(
    "--port",
    required=False,
    default=5672,
    type=int,
    show_default=True,
    help="Server port",
)
@click.option(
    "--username",
    required=False,
    default="guest",
    type=str,
    show_default=True,
    help="User account",
)
@click.option(
    "--password",
    required=False,
    default="guest",
    type=str,
    show_default=True,
    hide_input=True,
    help="User password",
)
@click.help_option("-h", "--help")
def cli(server, virtual_host, ssl, port, username, password):
    """Entry point for command."""
    credentials = pika.PlainCredentials(username, password)
    parameters = pika.ConnectionParameters(
        host=server,
        port=port,
        virtual_host=virtual_host,
        credentials=credentials,
    )

    try:
        connection = pika.BlockingConnection(parameters)
        if connection.is_open:
            print("OK")
            connection.close()
            exit(0)
    except Exception as error:
        print(f"Error: {error.__class__.__name__}")
        exit(1)
