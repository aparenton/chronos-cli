import copy
import json
import yaml

from chronos.exceptions import ChronosException


class Artifact:
    def __init__(self, from_conf):
        self._conf = from_conf

    def __setitem__(self, key, value):
        last_dot = key.rfind('.')
        self.__getitem__(key[:last_dot])[key[last_dot + 1:]] = value

    def __getitem__(self, key):
        path = [] if not key else key.split(".")
        return reduce(lambda d, k: d[k], path, self._conf)

    @property
    def conf(self):
        return self._conf

    @property
    def json(self):
        return json.dumps(self._conf)


def load_artifact(profile_names, filename, tag=None):
    try:
        with open(filename, 'r') as fp:
            artifact_conf = yaml.load(fp.read())
            return Artifact(artifact_conf)
    except IOError:
        raise ChronosException("{} WARNING: Job file %s not found" % filename)
