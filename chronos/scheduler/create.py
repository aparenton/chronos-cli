import json

import requests

from chronos.constants import default_headers, parent_parser
from chronos.config import load_server
from chronos.models import load_artifact
from chronos.outputter import print_json, result_json


def create_job(server, artifact, dry_run=False):
    url = "%s/v1/scheduler/iso8601" % server.url

    if dry_run:
        return {
            'artifact': artifact.conf,
            'server': server.__dict__
        }
    else:
        r = requests.post(url, artifact.json, auth=(server.username, server.password), headers=default_headers)
        return result_json(r.status_code, 'Scheduled job added')


def run(args):
    server = load_server(args.profile, args.config)
    artifact = load_artifact(args.profile, args.message)
    result = create_job(server, artifact, args.dry_run)
    print_json(result)


def register_command(subparsers):
    parser = subparsers.add_parser('create', parents=[parent_parser], help='Create a scheduled job')
    parser.set_defaults(func=run)

    parser.add_argument("--dry-run", action='store_true', help="Dry-run this command without really executing")
    parser.add_argument("-m", "--message", type=str, default="ChronosFile",
                        help="Chronos description file for the job")
