import json

import requests

from chronos.constants import default_headers, parent_parser
from chronos.config import load_server
from chronos.outputter import print_json


def list_jobs(server, cmd=""):
    url = "%s/v1/scheduler/jobs" % server.url
    r = requests.get(url, auth=(server.username, server.password), headers=default_headers)
    return json.loads(r.text) if r.text else {}


def run(args):
    server = load_server(args.profile, args.config)
    result = list_jobs(server)
    print_json(result)


def register_command(subparsers):
    parser = subparsers.add_parser('list', parents=[parent_parser], help='List all jobs')
    parser.set_defaults(func=run)
