import argparse

from .base_parser import BaseArguments, ArgumentError
from .. import types


class CliArgumentError(ArgumentError):
    pass


class CliArguments(BaseArguments):
    def _add_help(self):
        super(CliArguments, self)._add_help()
        for arg in self._attr_map.values():
            self._help[arg.name].append(f'[CLI] --{arg.name.replace("_", "-")}')

    def _parse(self):
        super(CliArguments, self)._parse()
        p = argparse.ArgumentParser()
        for arg in self._attr_map.values():
            p.add_argument(f'--{arg.name.replace("_", "-")}', type=str)

        args = p.parse_known_args()[0]
        for arg in self._attr_map.values():
            value = args.__getattribute__(arg.name)
            if value is None:
                continue
            try:
                value = types.parse_from_str(value, arg.type)
            except Exception as e:
                self._show_help()
                raise CliArgumentError(f"error parsing argument {arg.name} from Cli: {e}")

            self.__setattr__(arg.name, value)
            self._comes_from[arg.name] = "CLI    "
