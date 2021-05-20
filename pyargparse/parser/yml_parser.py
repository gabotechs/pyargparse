from .base_parser import BaseArguments, ArgumentError
import os
from .. import types
import yaml


class YamlParseError(ArgumentError):
    pass


class YmlArguments(BaseArguments):
    def _add_help(self):
        super(YmlArguments, self)._add_help()
        for arg in self._attr_map.values():
            self._help[arg.name].append(f'[YML] {arg.name}')

    def _parse(self):
        super(YmlArguments, self)._parse()
        path = self._config_path
        if not path or not os.path.isfile(path):
            return

        yaml_args = yaml.load(open(path), Loader=yaml.CLoader)
        for arg in self._attr_map.values():
            if yaml_args is None or arg.name not in yaml_args:
                continue
            value = yaml_args[arg.name]
            try:
                value_type = types.get_var_type(value)
            except ValueError as ve:
                self._show_help()
                raise YamlParseError(f"error getting type of argument '{arg.name}' in .yml file: {ve}")
            if value_type != arg.type:
                self._show_help()
                raise YamlParseError(f"value for argument '{arg.name}' on .yml file has type {value_type}, but type "
                                     f"{arg.type} was expected")

            self.__setattr__(arg.name, value)
            self._comes_from[arg.name] = "YML    "
