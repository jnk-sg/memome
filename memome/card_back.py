from memome_object import MemoMeObject
import repr_utils as ru


class CardBack(MemoMeObject):
    def __init__(self, s_back: str, s_obj_id: str):
        super().__init__(s_obj_id, "CardBack")
        self.s_back: str = s_back

    def __str__(self) -> str:
        return ru.obj_to_str(self, "CardBack", 0)

    def to_json(self) -> dict:
        d_card_back: dict = super().to_json()
        d_card_back["s_back"] = self.s_back
        return d_card_back
