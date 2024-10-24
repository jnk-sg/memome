import repr_utils as ru
from utils import generate_id
from card import Card


class Deck:
    def __init__(self, s_title: str,  s_deck_id: str = ""):
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
