import json

import requests

from chronos.constants import default_headers, parent_parser
from chronos.config import load_server
from chronos.outputter import print_json, result_json


def start_job(server, job_id):
    url = "%s/v1/scheduler/job/%s" % (server.url, job_id)

    r = requests.put(url, auth=(server.username, server.password), headers=default_headers)
    return result_json(r.status_code, 'Scheduled job started')


def run(args):
    server = load_server(args.profile, args.config)
    result = start_job(server, args.job)
    print(result)


def register_command(subparsers):
    parser = subparsers.add_parser('start', parents=[parent_parser], help='Start a job manually')
    parser.set_defaults(func=run)

    parser.add_argument("job", type=str, help="Name of the job")
