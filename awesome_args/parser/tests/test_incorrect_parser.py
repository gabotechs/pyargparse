from ..cli_parser import CliArguments
from ..env_parser import EnvArguments
from ..yml_parser import YmlArguments
from ..base_parser import BaseArguments, ArgumentError

from .arg_emulator import emulate_env, emulate_yml, emulate_cli
import typing as T
import pytest


class Args:
    mandatory_arg: int
    optional_arg: T.Optional[int]
    default_arg: int = 1
    default_optional_arg: T.Optional[int] = 3


class CliArgs(Args, CliArguments, BaseArguments):
    pass


class EnvArgs(Args, EnvArguments, BaseArguments):
    pass


class YmlArgs(Args, YmlArguments, BaseArguments):
    pass


parametrized_emulators = [
    pytest.param((emulate_cli, CliArgs), id="cli"),
    pytest.param((emulate_env, EnvArgs), id="env"),
    pytest.param((emulate_yml, YmlArgs), id="yml")
]


@pytest.mark.parametrize("emulators", parametrized_emulators)
def test_non_present_mandatory_arg(emulators: T.Tuple[T.Callable, T.Type[Args]]):
    context, Arguments = emulators
    with context({"mandatory_arg_BAAAD": 1}):
        try:
            Arguments()
            raise Exception()
        except ArgumentError:
            pass


@pytest.mark.parametrize("emulators", parametrized_emulators)
def test_incorrect_type_mandatory_arg(emulators: T.Tuple[T.Callable, T.Type[Args]]):
    context, Arguments = emulators
    with context({"mandatory_arg": ["bad", "really"]}):
        try:
            Arguments()
            raise Exception()
        except ArgumentError:
            pass


@pytest.mark.parametrize("emulators", parametrized_emulators)
def test_incorrect_type_optional_arg(emulators: T.Tuple[T.Callable, T.Type[Args]]):
    context, Arguments = emulators
    with context({"mandatory_arg": "correct", "optional_arg": ["bad"]}):
        try:
            Arguments()
            raise Exception()
        except ArgumentError:
            pass
