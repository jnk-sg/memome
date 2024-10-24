from memome.utils import repr_utils as ru
from memome_object import MemoMeObject
from card import Card


class Deck(MemoMeObject):
    def __init__(self, s_title: str,  s_obj_id: str):
        super().__init__(s_obj_id, "Deck")
        self.s_title: str = s_title
        self.d_cards: dict = {}

    def __str__(self) -> str:
        return ru.obj_to_str(self, "Deck", 0)

    def add_card(self, new_card: Card) -> None:
        self.d_cards[new_card.s_obj_id] = new_card

    def rem_card(self, s_card_id: str) -> None:
        self.d_cards.pop(s_card_id)

    def get_card(self, s_card_id: str) -> Card:
        return self.d_cards[s_card_id]

    def to_json(self) -> dict:
        d_deck: dict = super().to_json()
        d_deck["s_title"] = self.s_title
        d_deck["d_cards"] = {}
        for key in self.d_cards.keys():
            card: Card = self.d_cards[key]
            d_deck["d_cards"][card.s_obj_id] = card.to_json()
        return d_deck
