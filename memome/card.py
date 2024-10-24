from utils import generate_id
import repr_utils as ru
from card_front import CardFront
from card_back import CardBack


class Card:
    def __init__(self, s_title: str, c_front: CardFront, c_back: CardBack, s_card_id: str = ""):
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

