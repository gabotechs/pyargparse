from ..env_parser import EnvArguments
from ..base_parser import BaseArguments
import os
import typing as T


class Arguments(EnvArguments, BaseArguments):
    mandatory_arg: str
    optional_arg: T.Optional[str]
    default_arg: int = 1
    default_optional_arg: T.Optional[int] = 3


def test_correct_mandatory_arg_parse():
    os.environ["MANDATORY_ARG"] = "correct"
    args = Arguments()
    assert args.mandatory_arg == "correct"
    assert args.optional_arg is None
    assert args.default_arg == 1


def test_correct_optional_arg_parse():
    os.environ["MANDATORY_ARG"] = "correct"
    os.environ["OPTIONAL_ARG"] = "correct"
    args = Arguments()
    assert args.mandatory_arg == "correct"
    assert args.optional_arg == "correct"
    assert args.default_arg == 1


def test_correct_default_with_no_arg_parse():
    os.environ["MANDATORY_ARG"] = "correct"
    if os.environ.get("OPTIONAL_ARG", None):
        os.environ.pop("OPTIONAL_ARG")

    args = Arguments()
    assert args.mandatory_arg == "correct"
    assert args.optional_arg is None
    assert args.default_arg == 1


def test_correct_default_with_arg_parse():
    os.environ["MANDATORY_ARG"] = "correct"
    if os.environ.get("OPTIONAL_ARG", None):
        os.environ.pop("OPTIONAL_ARG")
    os.environ["DEFAULT_ARG"] = "2"
    args = Arguments()
    assert args.mandatory_arg == "correct"
    assert args.optional_arg is None
    assert args.default_arg == 2


def test_correct_default_optional_with_no_arg_parse():
    os.environ["MANDATORY_ARG"] = "correct"
    if os.environ.get("OPTIONAL_ARG", None):
        os.environ.pop("OPTIONAL_ARG")
    if os.environ.get("DEFAULT_OPTIONAL_ARG", None):
        os.environ.pop("DEFAULT_OPTIONAL_ARG")
    args = Arguments()
    assert args.mandatory_arg == "correct"
    assert args.optional_arg is None
    assert args.default_optional_arg == 3


def test_correct_default_optional_with_arg_parse():
    os.environ["MANDATORY_ARG"] = "correct"
    if os.environ.get("OPTIONAL_ARG", None):
        os.environ.pop("OPTIONAL_ARG")
    os.environ["DEFAULT_OPTIONAL_ARG"] = "5"
    args = Arguments()
    assert args.mandatory_arg == "correct"
    assert args.optional_arg is None
    assert args.default_optional_arg == 5
