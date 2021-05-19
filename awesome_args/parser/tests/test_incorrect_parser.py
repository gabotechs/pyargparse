from ..cli_parser import CliArguments
from ..base_parser import BaseArguments
import sys
import typing as T


class Arguments(CliArguments, BaseArguments):
    mandatory_arg: str
    optional_arg: T.Optional[str]
    default_arg: int = 1
    default_optional_arg: T.Optional[int] = 3
