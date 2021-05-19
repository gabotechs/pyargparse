import typing as T

import pytest

from .arg_emulator import emulate_cli, emulate_yml, emulate_env
from ..base_parser import BaseArguments
from ..cli_parser import CliArguments
from ..env_parser import EnvArguments
from ..yml_parser import YmlArguments


class Args:
    mandatory_arg: str
    optional_arg: T.Optional[str]
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
def test_correct_mandatory_arg_parse(emulators: T.Tuple[T.Callable, T.Type[Args]]):
    context, Arguments = emulators
    with context({"mandatory_arg": "correct"}):
        args = Arguments()
        assert args.mandatory_arg == "correct"
        assert args.optional_arg is None
        assert args.default_arg == 1


@pytest.mark.parametrize("emulators", parametrized_emulators)
def test_correct_optional_arg_parse(emulators: T.Tuple[T.Callable, T.Type[Args]]):
    context, Arguments = emulators
    with context({"mandatory_arg": "correct", "optional_arg": "correct"}):
        args = Arguments()
        assert args.mandatory_arg == "correct"
        assert args.optional_arg == "correct"
        assert args.default_arg == 1


@pytest.mark.parametrize("emulators", parametrized_emulators)
def test_correct_default_with_no_arg_parse(emulators: T.Tuple[T.Callable, T.Type[Args]]):
    context, Arguments = emulators
    with context({"mandatory_arg": "correct"}):
        args = Arguments()
        assert args.mandatory_arg == "correct"
        assert args.optional_arg is None
        assert args.default_arg == 1


@pytest.mark.parametrize("emulators", parametrized_emulators)
def test_correct_default_with_arg_parse(emulators: T.Tuple[T.Callable, T.Type[Args]]):
    context, Arguments = emulators
    with context({"mandatory_arg": "correct", "default_arg": "2"}):
        args = Arguments()
        assert args.mandatory_arg == "correct"
        assert args.optional_arg is None
        assert args.default_arg == 2


@pytest.mark.parametrize("emulators", parametrized_emulators)
def test_correct_default_optional_with_no_arg_parse(emulators: T.Tuple[T.Callable, T.Type[Args]]):
    context, Arguments = emulators
    with context({"mandatory_arg": "correct"}):
        args = Arguments()
        assert args.mandatory_arg == "correct"
        assert args.optional_arg is None
        assert args.default_optional_arg == 3


@pytest.mark.parametrize("emulators", parametrized_emulators)
def test_correct_default_optional_with_arg_parse(emulators: T.Tuple[T.Callable, T.Type[Args]]):
    context, Arguments = emulators
    with context({"mandatory_arg": "correct", "default_optional_arg": "5"}):
        args = Arguments()
        assert args.mandatory_arg == "correct"
        assert args.optional_arg is None
        assert args.default_optional_arg == 5
