from ..cli_parser import CliArguments
from ..base_parser import BaseArguments
import sys
import typing as T


class Arguments(CliArguments, BaseArguments):
    mandatory_arg: str
    optional_arg: T.Optional[str]
    default_arg: int = 1
    default_optional_arg: T.Optional[int] = 3


def test_correct_mandatory_arg_parse():
    sys.argv = [sys.argv[0], '--mandatory-arg', 'correct']
    args = Arguments()
    assert args.mandatory_arg == "correct"
    assert args.optional_arg is None
    assert args.default_arg == 1


def test_correct_optional_arg_parse():
    sys.argv = [sys.argv[0], '--mandatory-arg', 'correct', '--optional-arg', 'correct']
    args = Arguments()
    assert args.mandatory_arg == "correct"
    assert args.optional_arg == "correct"
    assert args.default_arg == 1


def test_correct_default_with_no_arg_parse():
    sys.argv = [sys.argv[0], '--mandatory-arg', 'correct']
    args = Arguments()
    assert args.mandatory_arg == "correct"
    assert args.optional_arg is None
    assert args.default_arg == 1


def test_correct_default_with_arg_parse():
    sys.argv = [sys.argv[0], '--mandatory-arg', 'correct', '--default-arg', '2']
    args = Arguments()
    assert args.mandatory_arg == "correct"
    assert args.optional_arg is None
    assert args.default_arg == 2


def test_correct_default_optional_with_no_arg_parse():
    sys.argv = [sys.argv[0], '--mandatory-arg', 'correct']
    args = Arguments()
    assert args.mandatory_arg == "correct"
    assert args.optional_arg is None
    assert args.default_optional_arg == 3


def test_correct_default_optional_with_arg_parse():
    sys.argv = [sys.argv[0], '--mandatory-arg', 'correct', '--default-optional-arg', '5']
    args = Arguments()
    assert args.mandatory_arg == "correct"
    assert args.optional_arg is None
    assert args.default_optional_arg == 5
