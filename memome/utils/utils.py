"""
    Modulo di utilities generico
"""

# TODO:

from random import choices

from loguru import logger

L_ALPHA_NUM = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z']
ID_LEN = 16


def generate_id(s_id_prefix: str = "", s_id_postfix: str = "") -> str:
    return s_id_prefix + "".join(choices(L_ALPHA_NUM, k=ID_LEN)) + s_id_postfix


if __name__ == "__main__":
    for i in range(4):
        print(generate_id("ID_"))

    print(type(None).__name__)
