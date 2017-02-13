import json

import requests

from chronos.constants import default_headers, parent_parser
from chronos.config import load_server
from chronos.outputter import print_json, result_json


def delete_job(server, job_id):
    url = "%s/v1/scheduler/job/%s" % (server.url, job_id)

    r = requests.delete(url, auth=(server.username, server.password), headers=default_headers)
    return result_json(r.status_code, 'Job deleted')


def run(args):
    server = load_server(args.profile, args.config)
    result = delete_job(server, args.job)
    print_json(result)


def register_command(subparsers):
    parser = subparsers.add_parser('delete', parents=[parent_parser], help='Delete a job')
    parser.set_defaults(func=run)

    parser.add_argument("job", type=str, help="Name of the job")
