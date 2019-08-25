"""
Tests connections to RabbitMQ Servers
"""

import argparse
import pika

parser = argparse.ArgumentParser(
    description='Check connection to RabbitMQ server'
)

parser.add_argument(
    '--server',
    required=True,
    help='Define RabbitMQ server'
)
parser.add_argument(
    '--virtual-host',
    default='/',
    help='Define virtual host'
)

parser.add_argument(
    '--ssl',
    action='store_true',
    help='Enable SSL (default: %(default)s)'
)
parser.add_argument(
    '--port',
    type=int,
    default=5672,
    help='Define port (default: %(default)s)'
)
parser.add_argument(
    '--user',
    default='guest',
    help='Define username (default: %(default)s)'
)
parser.add_argument(
    '--pass',
    default='guest',
    help='Define password (default: %(default)s)'
)
args = vars(parser.parse_args())


def main():
    print('Checking Connection...')
    credentials = pika.PlainCredentials(
        args['user'],
        args['pass']
    )
    parameters = pika.ConnectionParameters(
        host=args['server'],
        port=args['port'],
        virtual_host=args['virtual_host'],
        credentials=credentials
    )

    try:
        connection = pika.BlockingConnection(parameters)
        if connection.is_open:
            print('OK')
            connection.close()
            exit(0)
    except Exception as error:
        print('Error:', error.__class__.__name__)
        exit(1)


if __name__ == "__main__":
    main()
