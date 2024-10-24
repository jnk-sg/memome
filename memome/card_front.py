from base_obj import BaseObj
from memome.utils import repr_utils as ru


class CardFront(BaseObj):
    def __init__(self, s_front: str, s_obj_id: str):
        super().__init__(s_obj_id, "CardFront")
        self.s_front: str = s_front

    def __str__(self) -> str:
        return ru.obj_to_str(self, "CardFront", 0)

    def to_json(self) -> dict:
        d_card_front: dict = super().to_json()
        d_card_front["s_front"] = self.s_front
        return d_card_front
