import enum
import colorama as cr
from loguru import logger


def var_repr(s_name: str, s_type_name: str) -> str:
    return (cr.Fore.BLUE + s_name +
            cr.Fore.YELLOW + ": " +
            cr.Fore.CYAN + s_type_name +
            cr.Fore.YELLOW + " = ")


def int_repr(s_name: str, i_value: int) -> str:
    return var_repr(s_name, "int") + cr.Fore.RED + f"{i_value}"


def float_repr(s_name: str, f_value: float) -> str:
    return var_repr(s_name, "float") + cr.Fore.RED + f"{f_value}"


def complex_repr(s_name: str, f_value: complex) -> str:
    return var_repr(s_name, "float") + cr.Fore.RED + f"{f_value}"


def str_repr(s_name: str, s_value: str) -> str:
    return var_repr(s_name, "str") + cr.Fore.RED + f"'{s_value}'"


def is_primitive_type(obj: object) -> bool:
    return True if type(obj) is int or type(obj) is float or type(obj) is complex or type(obj) is str or type(obj) is bool else False


def obj_to_str(obj: object, s_obj_name: str, i_deep_level: int) -> str:
    if type(obj) is int:
        return cr.Fore.YELLOW + "\t" * i_deep_level + int_repr(s_obj_name, obj) + "\n"
    elif type(obj) is float:
        return cr.Fore.YELLOW + "\t" * i_deep_level + float_repr(s_obj_name, obj) + "\n"
    elif type(obj) is complex:
        return cr.Fore.YELLOW + "\t" * i_deep_level + complex_repr(s_obj_name, obj) + "\n"
    elif type(obj) is str:
        return cr.Fore.YELLOW + "\t" * i_deep_level + str_repr(s_obj_name, obj) + "\n"
    elif type(obj) is list:
        s_obj_str = (cr.Fore.YELLOW + "\t" * i_deep_level + s_obj_name +
                     cr.Fore.GREEN + ": " + cr.Fore.BLUE + "list" +
                     cr.Fore.GREEN + " = \n")
        for index, elem in enumerate(obj):
            s_tab = "\t" if is_primitive_type(elem) else ""
            s_obj_str += s_tab + obj_to_str(elem, str(index), i_deep_level + 1)
        return s_obj_str
    elif type(obj) is tuple:
        s_obj_str = (cr.Fore.YELLOW + "\t" * i_deep_level + s_obj_name +
                     cr.Fore.GREEN + ": " + cr.Fore.BLUE + "tuple" +
                     cr.Fore.GREEN + " = \n")
        for index, elem in enumerate(obj):
            s_tab = "\t" if is_primitive_type(elem) else ""
            s_obj_str += s_tab + obj_to_str(elem, str(index), i_deep_level + 1)
        return s_obj_str
    elif type(obj) is set:
        s_obj_str = (cr.Fore.YELLOW + "\t" * i_deep_level + s_obj_name +
                     cr.Fore.GREEN + ": " + cr.Fore.BLUE + "set" +
                     cr.Fore.GREEN + " = \n")
        for index, elem in enumerate(obj):
            s_tab = "\t" if is_primitive_type(elem) else ""
            s_obj_str += s_tab + obj_to_str(elem, str(index), i_deep_level + 1)
        return s_obj_str
    elif type(obj) is dict:  # If the dict keys aren't str or int this fail !!!
        s_obj_str = (cr.Fore.YELLOW + "\t" * i_deep_level + s_obj_name +
                     cr.Fore.GREEN + ": " + cr.Fore.BLUE + "dict" +
                     cr.Fore.GREEN + " = \n")
        for key in obj.keys():
            key_to_pass = key if type(key) is str else str(key)  # if the key is an int HERE fail so I must convert it
            s_obj_str += obj_to_str(obj[key], key_to_pass, i_deep_level + 1)
        return s_obj_str
    elif obj is None:
        logger.error("TODO: write code for NoneType !!!")
        return "NO REPR"
    else:  # if not a built-in type
        d_attr = obj.__dict__
        s_obj_str = ("\t" * i_deep_level +
                     cr.Fore.YELLOW + s_obj_name +  # HERE fail if s_obj_name is int
                     cr.Fore.GREEN + ": " + cr.Fore.BLUE + type(obj).__name__ +
                     cr.Fore.GREEN + " = ...\n")
        for key in d_attr.keys():
            s_obj_str += obj_to_str(d_attr[key], key, i_deep_level + 1)
        return s_obj_str
