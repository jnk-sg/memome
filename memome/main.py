"""
Note:
    1 - in questo progetto al momento non ho voglia di gestire l'incapsulazione dei dati quindi niente getter o setter
"""

# TODO:
#   1 - creare un repository come fatto da chatgpt ma invece che di una stringa c'è l'oggetto
#   2 - nel module ru mettere il colore dei nomi delle variabili dei dati primiti simile a quello delle altre non proprio uguale ma simile in modo che ho subito a colpo d'occhio
#       quali sono i nomi delle variabili

import json

from memome.utils.utils import generate_id
from memome.utils import repr_utils as ru
from memome.utils import date_time_utils as dtu

from memome.card import Card, CardFront, CardBack
from memome.card_status import CardStatus
from memome.box import Box
from memome.leitner import Leitner
from user import User


class MemoMe:
    def __init__(self,s_repository_file_path_name: str, c_leitner: Leitner, c_user: User):
        self.s_repository_file_path_name: str = s_repository_file_path_name
        self.c_leitner: Leitner = c_leitner
        self.c_user: User = c_user

    def __str__(self) -> str:
        return ru.obj_to_str(self, "MemoMe", 0)

    def to_json(self) -> dict:
        return {
            self.c_leitner.s_obj_id: self.c_leitner.to_json(),
            self.c_user.s_obj_id: self.c_user.to_json()
        }

    def load_repository(self) -> None:
        pass

    def save_repository(self) -> None:
        with open(self.s_repository_file_path_name, "w") as data_file:
            json.dump(self.to_json(), data_file)


if __name__ == "__main__":
    from pprint import pprint

    u0: User = User("Ste", "ste_pwd", generate_id("USER_", "_ID"))

    c0: Card = Card("Carta 0", CardFront("Fronte 0", generate_id("CARD_FRONT_", "_ID")), CardBack("Back 0", generate_id("CARD_BACK_", "_ID")), generate_id("CARD_", "_ID"))
    c1: Card = Card("Carta 1", CardFront("Fronte 1", generate_id("CARD_FRONT_", "_ID")), CardBack("Back 1", generate_id("CARD_BACK_", "_ID")), generate_id("CARD_", "_ID"))
    c2: Card = Card("Carta 2", CardFront("Fronte 2", generate_id("CARD_FRONT_", "_ID")), CardBack("Back 2", generate_id("CARD_BACK_", "_ID")), generate_id("CARD_", "_ID"))

    cs0: CardStatus = CardStatus(u0.s_obj_id, c0.s_obj_id, dtu.now_date_time(), generate_id("CARD_STATUS_", "_ID"))
    cs1: CardStatus = CardStatus(u0.s_obj_id, c1.s_obj_id, dtu.now_date_time(), generate_id("CARD_STATUS_", "_ID"))
    cs2: CardStatus = CardStatus(u0.s_obj_id, c2.s_obj_id, dtu.now_date_time(), generate_id("CARD_STATUS_", "_ID"))

    box1: Box = Box("Box 1", 1, generate_id("BOX_", "_ID"))
    box2: Box = Box("Box 2", 2, generate_id("BOX_", "_ID"))
    box3: Box = Box("Box 3", 4, generate_id("BOX_", "_ID"))

    box1.add_card_status(cs0)
    box1.add_card_status(cs2)
    box2.add_card_status(cs1)

    leitner: Leitner = Leitner("Leitner Algoritmo", generate_id("LEITNER_", "_ID"))
    leitner.add_box(box1)
    leitner.add_box(box2)
    leitner.add_box(box3)

    pprint(leitner.to_json())

    c_memome = MemoMe("../data/repository.json", leitner, u0)
    c_memome.save_repository()

