from contextlib import contextmanager
import sys
import os


@contextmanager
def emulate_cli(d: dict):
    args = []
    for k, v in d.items():
        args.append("--"+k.replace("_", "-"))
        args.append(str(v) if not type(v) == list else ",".join([str(x) for x in v]))
    sys.argv = [sys.argv[0], *args]
    yield None
    sys.argv = [sys.argv[0]]


@contextmanager
def emulate_env(d: dict):
    for k, v in d.items():
        os.environ[k.upper()] = str(v) if not type(v) == list else ",".join([str(x) for x in v])
    yield None
    for k in d:
        os.environ.pop(k.upper())


@contextmanager
def emulate_yml(d: dict):
    yml = ""
    for k, v in d.items():
        yml += k+": "
        if type(v) == list:
            for el in v:
                yml += "\n- "+str(el)
        else:
            yml += str(v)
        yml += "\n"
    with open("config.yml", "w") as f:
        f.write(yml)
    yield None
    os.remove("config.yml")
