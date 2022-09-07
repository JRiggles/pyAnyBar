#!/usr/bin/env python
import socket


colors = [
    'white', 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple',
    'black', 'question', 'exclamation', 'none', 'filled', 'hollow'
]


class AnyBar():
    def __init__(self, port=1738, address='localhost'):
        self.port = port
        self.address = address
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def set(self, color, text=None):
        if color not in colors:
            raise ValueError(
                ('Color is not valid. It must be one of the '
                 f'following: {", ".join(colors)}')
        )

        if text is None:
            self.socket.sendto(
                color.encode('utf-8'),
                (self.address, self.port)
            )
        else:
            message = f'{color} {text}'
            self.socket.sendto(message, (self.address, self.port))


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Change the color of AnyBar')
    parser.add_argument(
        'color',
        choices=colors,
        help='The color you want to change to.'
    )
    parser.add_argument(
        'port',
        type=int,
        nargs='?',
        default=1738,
        help='The port of the AnyBar instance (default: 1738).'
    )
    parser.add_argument(
        'address',
        nargs='?',
        default='localhost',
        help='The address of the AnyBar instance (default: localhost).'
    )
    args = parser.parse_args()

    AnyBar(port=args.port, address=args.address).set(args.color)

