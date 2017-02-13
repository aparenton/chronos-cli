# Chronos CLI

A Command-line Interface for [Chronos v3](https://github.com/mesos/chronos/releases/tag/v3.0.0).

## Installation

Directly from GitHub:

```shell
# latest version (use @version for specific version)
$ pip install git+ssh://git@github.com/aparenton/chronos-cli.git
```

Or, install from the sources after cloning:

```shell
$ python setup.py install
```

## Configuration

Chronos CLI supports both YAML and JSON (see [config](config)):

```yaml
stage:
  url: YOUR_CHRONOS_STAGE_URL
  username: YOUR_CHRONOS_STAGE_USERNAME
  password: YOUR_CHRONOS_STAGE_PASSWORD
prod:
  url: YOUR_CHRONOS_PROD_URL
  username: YOUR_CHRONOS_PROD_USERNAME
  password: YOUR_CHRONOS_PROD_PASSWORD
```

By default, Chronos CLI will read from:

- `~/.config/chronos/config.json` or
- `~/.config/chronos/config.yaml` or
- `~/.config/chronos/config.yml`

But you can choose a specific configuration file with `--config my-config.yaml`.

## Chronos artifact

A simple Chronos artifact (see [examples](examples) for more detailed samples):

```json
{
  "schedule":"R/2015-11-09T00:00:00Z/PT24H",
  "name":"test-1",
  "epsilon":"PT30M",
  "command":"echo test1 && sleep 60",
  "owner":"user@domain.com",
  "async":false
}
```

Note: see [Chronos documentation for ISO 8601 format for scheduling the job.](https://mesos.github.io/chronos/docs/api.html#adding-a-scheduled-job)

## Usage

```shell
$ chronos -h
usage: chronos [-h] {create_dep,create,delete,get,graph,kill,list,start} ...

positional arguments:
  {create_dep,create,delete,get,graph,kill,list,start}
                        Description
    create_dep          Create a dependent job
    create              Create a scheduled job
    delete              Delete a job
    get                 Get filtered jobs
    graph               Dependency graph
    kill                Kill all tasks for a job
    list                List all jobs
    start               Start a job manually

optional arguments:
  -h, --help            show this help message and exit
```

You can also do:

```shell
$ chronos create -h
usage: chronos create [-h] [-p PROFILE] [-c CONFIG] [--dry-run] [-m MESSAGE]

optional arguments:
  -h, --help            show this help message and exit
  -p PROFILE, --profile PROFILE
                        Profile to run
  -c CONFIG, --config CONFIG
                        Config file for chronos
  --dry-run             Dry-run this command without really executing
  -m MESSAGE, --message MESSAGE
                        Chronos description file for the job
```

## Example

So if you want to create a new scheduled job on Chronos using Chronos CLI, you would do:

```shell
$ chronos create -m examples/sample-job.json -p stage
{
    "message": "Scheduled job added",
    "code": 204
}
```

**Note: by default `stage` is being used as your profile.**
