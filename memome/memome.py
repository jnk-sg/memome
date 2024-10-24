"""
Note:
    1 - in questo progetto al momento non ho voglia di gestire l'incapsulazione dei dati quindi niente getter o setter
"""

# TODO:
#   1 - creare un repository come fatto da chatgpt ma invece che di una stringa c'è l'oggetto
#   2 - nel module ru mettere il colore dei nomi delle variabili dei dati primiti simile a quello delle altre non proprio uguale ma simile in modo che ho subito a colpo d'occhio
#       quali sono i nomi delle variabili

import json
import pprint

from loguru import logger

from utils import generate_id
from sgs_enum import SGSEnum
import repr_utils as ru
import date_time_utils as dtu
from objects_repository import ObjectsRepository


if __name__ == "__main__":
    obj_rep = ObjectsRepository("./repository.json")

    # TODO: mettere su un sistema grafico semplice per testare il tutto con dati immessi manualmente
    c0 = Card("Carta 0", CardFront("Fronte 0"), CardBack("Back 0"))
    c1 = Card("Carta 1", CardFront("Fronte 1"), CardBack("Back 1"))
    c2 = Card("Carta 2", CardFront("Fronte 2"), CardBack("Back 2"))
    d0 = Deck("Mazzo 0")
    d0.add_card(c0)
    d0.add_card(c1)
    d0.add_card(c2)

    u0 = CardUser("Ste", "pwd_ste")
    cs0 = CardStatus(u0.s_user_id, c0.s_card_id, dtu.now_date_time())
    cs2 = CardStatus(u0.s_user_id, c1.s_card_id, dtu.now_date_time())
    cs1 = CardStatus(u0.s_user_id, c2.s_card_id, dtu.now_date_time())
