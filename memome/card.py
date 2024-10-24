from memome.utils import repr_utils as ru
from card_front import CardFront
from card_back import CardBack
from base_obj import BaseObj


class Card(BaseObj):
    def __init__(self, s_title: str, c_front: CardFront, c_back: CardBack, s_obj_id: str):
        super().__init__(s_obj_id, "Card")
        self.s_title: str = s_title
        self.c_front: CardFront = c_front
        self.c_back: CardBack = c_back

    def __str__(self) -> str:
        return ru.obj_to_str(self, "Card", 0)

    def to_json(self) -> dict:
        d_card: dict = super().to_json()
        d_card["s_title"] = self.s_title
        d_card["c_front"] = self.c_front.to_json()
        d_card["c_back"] = self.c_back.to_json()
        return d_card
