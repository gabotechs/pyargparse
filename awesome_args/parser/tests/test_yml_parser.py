from ..yml_parser import YmlArguments
from ..base_parser import BaseArguments
import os
import typing as T


class Arguments(YmlArguments, BaseArguments):
    mandatory_arg: str
    optional_arg: T.Optional[str]
    default_arg: int = 1
    default_optional_arg: T.Optional[int] = 3


def test_correct_mandatory_arg_parse():
    with open("config.yml", "w") as f:
        f.write("mandatory_arg: correct\n")
    args = Arguments()
    assert args.mandatory_arg == "correct"
    assert args.optional_arg is None
    assert args.default_arg == 1
    os.remove("config.yml")


def test_correct_optional_arg_parse():
    with open("config.yml", "w") as f:
        f.write("mandatory_arg: correct\noptional_arg: correct\n")
    args = Arguments()
    assert args.mandatory_arg == "correct"
    assert args.optional_arg == "correct"
    assert args.default_arg == 1
    os.remove("config.yml")


def test_correct_default_with_no_arg_parse():
    with open("config.yml", "w") as f:
        f.write("mandatory_arg: correct\n")
    args = Arguments()
    assert args.mandatory_arg == "correct"
    assert args.optional_arg is None
    assert args.default_arg == 1
    os.remove("config.yml")


def test_correct_default_with_arg_parse():
    with open("config.yml", "w") as f:
        f.write("mandatory_arg: correct\ndefault_arg: 2\n")
    args = Arguments()
    assert args.mandatory_arg == "correct"
    assert args.optional_arg is None
    assert args.default_arg == 2
    os.remove("config.yml")


def test_correct_default_optional_with_no_arg_parse():
    with open("config.yml", "w") as f:
        f.write("mandatory_arg: correct\n")
    args = Arguments()
    assert args.mandatory_arg == "correct"
    assert args.optional_arg is None
    assert args.default_optional_arg == 3
    os.remove("config.yml")


def test_correct_default_optional_with_arg_parse():
    with open("config.yml", "w") as f:
        f.write("mandatory_arg: correct\ndefault_optional_arg: 5")
    args = Arguments()
    assert args.mandatory_arg == "correct"
    assert args.optional_arg is None
    assert args.default_optional_arg == 5
    os.remove("config.yml")
