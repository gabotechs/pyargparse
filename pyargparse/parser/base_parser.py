from abc import ABC
import typing as T
from .. import types
from collections import defaultdict


class ArgumentError(ValueError):
    pass


class ClassAttr:
    def __init__(self, name: str, type_, optional):
        self.name = name
        self.type = type_
        self.optional = optional


class BaseArguments(ABC):
    def __init__(self, config_path: str = "config.yml"):
        self._comes_from: T.Dict[str, str] = {}
        self._help: T.Dict[str, T.List[str]] = defaultdict(lambda: [])
        self._config_path = config_path
        self._attr_map = self.__get_args()
        self._add_help()
        self._parse()
        self.__validate()

    def __repr__(self):
        msg = "==== PROGRAM ARGUMENTS ====\n"
        for arg in self._attr_map.values():
            comes_from = "DEFAULT" if arg.name not in self._comes_from else self._comes_from[arg.name]
            msg += f"{comes_from} {arg.name}: {self.__getattribute__(arg.name)}\n"
        msg += "=========================="
        return msg

    def _add_help(self):
        pass

    def _parse(self):
        pass

    def __validate(self):
        for arg in self._attr_map.values():
            if not hasattr(self, arg.name) or not arg.optional and getattr(self, arg.name) is None:
                print(f"argument '{arg.name}' is mandatory, but no value was provided")
                self._show_help()
                raise ArgumentError(f"argument '{arg.name}' is mandatory, but no value was provided")

    def __get_args(self):
        if not hasattr(self, "__annotations__"):
            raise ArgumentError("at least one configuration parameter must be declared with an annotation")
        attr_map = {}
        for attr, annotation in self.__annotations__.items():
            try:
                annotation_type = types.get_annotation_type(annotation)
            except ValueError as ve:
                raise ArgumentError(f"error parsing annotation type for parameter '{attr}': {ve}")

            default_value = getattr(self, attr) if hasattr(self, attr) else None
            is_optional = types.annotation_is_optional(annotation)
            if default_value is not None:
                try:
                    default_type = types.get_var_type(default_value)
                except ValueError as ve:
                    raise ArgumentError(f"error processing type of the default value of '{attr}': {ve}")

                if default_type != annotation_type:
                    raise ArgumentError(
                        f"argument '{attr}' has a default value {default_value} of type {default_type}, "
                        f"but type {annotation_type} was expected"
                    )

                self.__setattr__(attr, default_value)
            elif is_optional:
                self.__setattr__(attr, default_value)

            attr_map[attr] = ClassAttr(
                attr,
                annotation_type,
                is_optional or default_value is not None
            )
        return attr_map

    def _show_help(self):
        for attr, parsers_help in self._help.items():
            arg = self._attr_map[attr]
            print(f"{attr} ({arg.type}){' (optional)' if arg.optional else ''}:")
            print("  ", "    ".join(parsers_help[::-1]))
