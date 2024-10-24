"""
Note:
    1 - in questo progetto al momento non ho voglia di gestire l'incapsulazione dei dati quindi niente getter o setter
"""

# TODO:
#   1 - creare un repository come fatto da chatgpt ma invece che di una stringa c'è l'oggetto

import json
import pprint

from loguru import logger

from utils import generate_id
from sgs_enum import SGSEnum
import repr_utils as ru
import date_time_utils as dt


class CardState(SGSEnum):
    SLEEPING = SGSEnum("SLEEPING", 1)
    TO_REVIEW = SGSEnum("TO_REVIEW", 2)
    OUT_OF_DATE = SGSEnum("OUT_OF_DATE", 4)


class CardUser:
    def __init__(self, s_user_name: str, s_user_pwd: str, s_user_id: str):
        self.s_user_id: str = generate_id("USER_", "_ID") if not s_user_id else s_user_id
        self.s_user_name: str = s_user_name
        self.s_user_pwd: str = s_user_pwd

    def __str__(self) -> str:
        return ru.obj_to_str(self, "CardUser", 0)
    
    def to_json(self) -> dict:
        return {
            "s_obj_type:": "CardUser",
            "s_user_id": self.s_user_id,
            "s_user_name": self.s_user_name,
            "s_user_pwd": self.s_user_pwd
        }

    def from_json(self, d_json_dict: dict) -> None:
        self.s_user_id = d_json_dict.get("s_user_id", generate_id(""))
        self.s_user_name = d_json_dict.get("s_user_name", generate_id(""))
        self.s_user_pwd = d_json_dict.get("s_user_pwd", generate_id(""))


class CardFront:
    def __init__(self, s_front: str):
        self.s_front: str = s_front

    def __str__(self) -> str:
        return ru.obj_to_str(self, "CardFront", 0)

    def to_json(self) -> dict:
        return {
            "s_front": self.s_front,
        }


class CardBack:
    def __init__(self, s_back: str):
        self.s_back: str = s_back

    def __str__(self) -> str:
        return ru.obj_to_str(self, "CardBack", 0)

    def to_json(self) -> dict:
        return {
            "s_back": self.s_back,
        }


class Card:
    def __init__(self, s_title: str, c_front: CardFront, c_back: CardBack, s_card_id: str):
        self.s_card_id: str = generate_id("CARD_", "_ID") if not s_card_id else s_card_id
        self.s_title: str = s_title
        self.c_front: CardFront = c_front
        self.c_back: CardBack = c_back

    def __str__(self) -> str:
        return ru.obj_to_str(self, "Card", 0)

    def to_json(self) -> dict:
        return {
            "s_card_id": self.s_card_id,
            "s_title": self.s_title,
            "c_front": self.c_front.to_json(),
            "c_back": self.c_back.to_json()
        }


class Deck:
    def __init__(self, s_title: str,  s_deck_id: str):
        self.s_deck_id: str = generate_id("DECK_", "_ID") if not s_deck_id else s_deck_id
        self.s_title: str = s_title
        self.d_cards: dict = {}

    def __str__(self) -> str:
        return ru.obj_to_str(self, "Deck", 0)

    def add_card(self, new_card: Card) -> None:
        self.d_cards[new_card.s_card_id] = new_card

    def rem_card(self, s_card_id: str) -> None:
        self.d_cards.pop(s_card_id)

    def get_card(self, s_card_id: str) -> Card:
        return self.d_cards[s_card_id]

    def to_json(self) -> dict:
        d_deck = {
            "s_deck_id": self.s_deck_id,
            "s_title": self.s_title,
            "d_cards": {}
        }
        for key in self.d_cards.keys():
            card: Card = self.d_cards[key]
            d_deck["d_cards"][card.s_card_id] = card.to_json()
        return d_deck


class CardStatus:
    def __init__(self, s_user_id: str, s_card_id: str, s_current_box_id: str, s_insert_date: str, e_card_state: CardState.TO_REVIEW, s_status_id: str):
        self.s_status_id: str = generate_id("STATUS_", "_ID") if not s_status_id else s_status_id
        self.s_user_id: str = s_user_id
        self.s_card_id: str = s_card_id
        self.s_insert_date: str = s_insert_date
        self.e_card_state: CardState = e_card_state

    def __str__(self) -> str:
        return ru.obj_to_str(self, "CardStatus", 0)

    def to_json(self) -> dict:
        return {
            "s_card_status_id": self.s_status_id,
            "s_user_id": self.s_user_id,
            "s_card_id": self.s_card_id,
            "s_insert_date": self.s_insert_date,
            "e_card_state": self.e_card_state.value
        }


class Box:
    def __init__(self, s_title: str, i_review_frequency: int, s_box_id: str):
        self.s_box_id: str = generate_id("BOX_", "_ID") if not s_box_id else s_box_id
        self.s_title: str = s_title
        self.i_review_frequency: int = i_review_frequency
        self.d_cards_status: dict = {}

    def __str__(self) -> str:
        return ru.obj_to_str(self, "Box", 0)

    def add_card_status(self, new_card_status: CardStatus) -> None:
        self.d_cards_status[new_card_status.s_card_id] = new_card_status

    def remove_card_status(self, s_id: str) -> None:
        self.d_cards_status.pop(s_id)

    def get_cards_status(self, s_user_id: str) -> list:
        l_cards_status = []
        for key in self.d_cards_status.keys():
            c_status: CardStatus = self.d_cards_status[key]
            if c_status.s_user_id == s_user_id:
                l_cards_status.append(c_status)
        return l_cards_status

    def get_cards_status_with_state(self, s_user_id: str, e_state: CardState) -> list:
        l_cards_status: list = []
        for key in self.d_cards_status.keys():
            c_status: CardStatus = self.d_cards_status[key]
            if c_status.s_user_id == s_user_id and c_status.e_card_state == e_state:
                l_cards_status.append(c_status)
        return l_cards_status

    def update_cards_status(self, s_date_time: str):
        for key in self.d_cards_status.keys():
            c_status: CardStatus = self.d_cards_status[key]
            i_delta_time = dt.delta_hours(s_date_time, c_status.s_insert_date)
            if i_delta_time < self.i_review_frequency:
                c_status.e_card_state = CardState.SLEEPING
            elif i_delta_time == self.i_review_frequency:
                c_status.e_card_state = CardState.TO_REVIEW
            elif i_delta_time > self.i_review_frequency:
                c_status.e_card_state = CardState.OUT_OF_DATE

    def to_json(self) -> dict:
        d_box = {
            "s_box_id": self.s_box_id,
            "s_title": self.s_title,
            "i_review_frequency": self.i_review_frequency,
            "d_cards_status": {}
        }
        for key in self.d_cards_status.keys():
            card: CardStatus = self.d_cards_status[key]
            d_box["d_cards_status"][card.s_status_id] = card.to_json()
        return d_box


class Leitner:
    def __init__(self, s_title: str, s_leitner_id: str):
        self.s_leitner_id: str = generate_id("LEITNER_","_ID") if not s_leitner_id else s_leitner_id
        self.s_title: str = s_title
        self.d_boxes: dict = {}

    def __str__(self) -> str:
        return ru.obj_to_str(self, "Leitner", 0)

    def add_box(self, new_box: Box) -> None:
        self.d_boxes[new_box.s_box_id] = new_box

    def remove_box(self, s_box_id: str) -> None:
        self.d_boxes.pop(s_box_id)

    def update_boxs_status(self, s_date_time: str):
        for key in self.d_boxes.keys():
            c_box: Box = self.d_boxes[key]
            c_box.update_cards_status(s_date_time)

    def to_json(self) -> dict:
        d_leitner = {
            "s_leitner_id": self.s_leitner_id,
            "s_title": self.s_title,
            "d_boxes": {}
        }
        for key in self.d_boxes.keys():
            box: Box = self.d_boxes[key]
            d_leitner["d_boxes"][box.s_box_id] = box.to_json()
        return d_leitner

    def save_data(self) -> None:
        with open("leitner.json", "w") as data_file:
            json.dump(self.to_json(), data_file)

    def load_data(self) -> None:
        # TODO: da fare
        #       creazione automatica delle classi ???
        d_leitner: dict = {}
        with open("leitner.json", "r") as data_file:
            d_leitner = json.load(data_file)

        self.s_leitner_id = d_leitner.get("s_leitner_id", generate_id(""))
        self.s_title = d_leitner.get("s_title", "")
        self.d_boxes = []


class ObjectsRepository:
    def __init__(self):
        self.d_repository: dict = {}

    def __str__(self) -> str:
        return ru.obj_to_str(self, "ObjectsRepository", 0)

    def add_obj(self, obj: object) -> None:
        self.d_repository[obj.]

    def rem_obj(self, s_obj_id: str) -> None:
        pass

    def get_obj(self, s_obj_id: str) -> object:
        pass


if __name__ == "__main__":
    # TODO: mettere su un sistema grafico semplice per testare il tutto con dati immessi manualmente

    carta_0 = Card("", "Carta 0", CardFront("Fronte 0"), CardBack("Back 0"))
    carta_1 = Card("", "Carta 0", CardFront("Fronte 1"), CardBack("Back 1"))
    carta_2 = Card("", "Carta 0", CardFront("Fronte 2"), CardBack("Back 2"))
    carta_3 = Card("", "Carta 0", CardFront("Fronte 3"), CardBack("Back 3"))
    carta_4 = Card("", "Carta 0", CardFront("Fronte 4"), CardBack("Back 4"))

    mazzo_0 = Deck("", "Mazzo 0")
    mazzo_0.add_card(carta_0)
    mazzo_0.add_card(carta_1)

    user_0 = CardUser("", "Pippo", "pwd_pippo")

    box_0 = Box("", "Prima Scatola", 1)
    box_0.add_card_status(CardStatus("", user_0.s_user_id, carta_0.s_card_id, box_0.s_box_id, dt.now_date_time(), CardState.TO_REVIEW))  # c'è un errore
    # e poi non capisco bene se fare una factory alla quale chidere gli oggetti e trasmettere la facotri oppure passare gli oggetti o passare gli ids

    pprint.pprint(mazzo_0.to_json())
    ru.obj_to_str(box_0.d_cards_status, "STATUS", 0)
