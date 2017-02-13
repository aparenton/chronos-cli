import json

import requests

from chronos.constants import default_headers, parent_parser
from chronos.config import load_server
from chronos.outputter import print_json


def search(server, job_id):
    url = "%s/v1/scheduler/jobs/search?name=%s" % (server.url, job_id)
    r = requests.get(url, auth=(server.username, server.password), headers=default_headers)
    return json.loads(r.text) if r.text else {}


def run(args):
    server = load_server(args.profile, args.config)
    result = search(server, args.job)
    print_json(result)


def register_command(subparsers):
    parser = subparsers.add_parser('search', parents=[parent_parser], help='Search for a job')
    parser.set_defaults(func=run)

    parser.add_argument("job", type=str, help="Name of the job")
