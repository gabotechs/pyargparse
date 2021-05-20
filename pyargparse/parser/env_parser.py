from .base_parser import BaseArguments, ArgumentError
import os
from .. import types


class EnvParseError(ArgumentError):
    pass


class EnvArguments(BaseArguments):
    def _add_help(self):
        super(EnvArguments, self)._add_help()
        for arg in self._attr_map.values():
            self._help[arg.name].append(f'[ENV] {arg.name.upper()}')

    def _parse(self):
        super(EnvArguments, self)._parse()
        for arg in self._attr_map.values():
            value = os.environ.get(arg.name.upper(), None)
            if value is None:
                continue
            try:
                value = types.parse_from_str(value, arg.type)
            except Exception as e:
                self._show_help()
                raise EnvParseError(f"error parsing argument {arg.name} from env variable: {e}")
            self.__setattr__(arg.name, value)
            self._comes_from[arg.name] = "ENV    "
