from .base_parser import ArgumentError, BaseArguments
from .env_parser import EnvParseError, EnvArguments
from .yml_parser import YamlParseError, YmlArguments
from .cli_parser import CliArguments, CliArgumentError


class CliArgs(CliArguments, BaseArguments):
    pass


class EnvArgs(EnvArguments, BaseArguments):
    pass


class YmlArgs(YmlArguments, BaseArguments):
    pass


class CliEnvArgs(CliArguments, EnvArguments, BaseArguments):
    pass


class CliYmlArgs(CliArguments, YmlArguments, BaseArguments):
    pass


class EnvYmlArgs(EnvArguments, YmlArguments, BaseArguments):
    pass


class PyArgs(CliArguments, EnvArguments, YmlArguments, BaseArguments):
    pass
