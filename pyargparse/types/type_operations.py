from typing import List, Union


class Types:
    STR = "str"
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    STR_L = "typing.List[str]"
    INT_L = "typing.List[int]"
    FLOAT_L = "typing.List[float]"


ALLOWED_TYPES = Types.STR, Types.INT, Types.FLOAT, Types.BOOL, Types.STR_L, Types.INT_L, Types.FLOAT_L


def get_optional_annotation(annotation):
    for possible_type in [str, int, float, bool, List[str], List[int], List[float]]:
        if annotation == Union[possible_type, None] or annotation == Union[None, possible_type]:
            return possible_type
    return None


def annotation_is_optional(annotation):
    optional_type = get_optional_annotation(annotation)
    return optional_type is not None


def get_annotation_type(annotation):
    optional_type = get_optional_annotation(annotation)
    ann_type = annotation if optional_type is None else optional_type

    if ann_type == str:
        return Types.STR
    elif ann_type == int:
        return Types.INT
    elif ann_type == float:
        return Types.FLOAT
    elif ann_type == bool:
        return Types.BOOL
    elif ann_type == List[str]:
        return Types.STR_L
    elif ann_type == List[int]:
        return Types.INT_L
    elif ann_type == List[float]:
        return Types.FLOAT_L
    else:
        raise ValueError(f"not allowed type annotation {ann_type}")


def get_var_type(var):
    var_type = type(var)
    if var_type == str:
        return Types.STR
    elif var_type == int:
        return Types.INT
    elif var_type == float:
        return Types.FLOAT
    elif var_type == bool:
        return Types.BOOL
    elif var_type == list:
        if len(var) == 0:
            raise ValueError(f"cannot determine the type of an empty list")
        list_type = None
        for el in var:
            if list_type is None:
                list_type = type(el)
            else:
                if list_type != type(el):
                    raise ValueError(f"all the elements in the list should have the same type, but found at least two "
                                     f"different types: {list_type} and {type(el)}")
        if list_type == str:
            return Types.STR_L
        elif list_type == int:
            return Types.INT_L
        elif list_type == float:
            return Types.FLOAT_L
        else:
            raise ValueError(f"the list must have an inner type of str, int or float, {list_type} is not allowed")
    else:
        raise ValueError(f"found not allowed type {var_type}")


def parse_from_str(var: str, var_type: str):
    if var_type == Types.STR:
        return str(var)
    elif var_type == Types.INT:
        return int(var)
    elif var_type == Types.FLOAT:
        return float(var)
    elif var_type == Types.BOOL:
        return str(var).lower() in ["true", "yes", "1"]
    elif var_type == Types.STR_L:
        return [x.strip() for x in var.split(",")]
    elif var_type == Types.INT_L:
        return [int(x.strip()) for x in var.split(",")]
    elif var_type == Types.FLOAT_L:
        return [float(x.strip()) for x in var.split(",")]
    else:
        raise ValueError(f"unsupported var type {var_type}")
