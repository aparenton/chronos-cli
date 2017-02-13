import json

import requests

from chronos.constants import default_headers, parent_parser
from chronos.config import load_server
from chronos.outputter import print_json


def graph(server, format='csv'):
    url = "%s/v1/scheduler/graph/%s" % (server.url, format)
    r = requests.get(url, auth=(server.username, server.password))
    return r.text


def run(args):
    server = load_server(args.profile, args.config)
    result = graph(server, args.format)
    print(result)


def register_command(subparsers):
    parser = subparsers.add_parser('graph', parents=[parent_parser], help='Dependency graph')
    parser.set_defaults(func=run)

    parser.add_argument("-f", "--format", default='csv', choices=['csv', 'dot'], help='Graph format')
