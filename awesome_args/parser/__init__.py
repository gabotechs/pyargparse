from .base_parser import ArgumentError, BaseArguments
from .env_parser import EnvParseError, EnvArguments
from .yml_parser import YamlParseError, YmlArguments
from .cli_parser import CliArguments, CliArgumentError


class AwesomeArguments(CliArguments, EnvArguments, YmlArguments, BaseArguments):
    pass
