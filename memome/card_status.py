from memome.utils import repr_utils as ru

from base_obj import BaseObj


class CardStatus(BaseObj):
    def __init__(self, s_user_id: str, s_card_id: str, s_insert_date: str, s_obj_id: str):
        super().__init__(s_obj_id, "CardStatus")
        self.s_user_id: str = s_user_id
        self.s_card_id: str = s_card_id
        self.s_insert_date: str = s_insert_date

    def __str__(self) -> str:
        return ru.obj_to_str(self, "CardStatus", 0)

    def to_json(self) -> dict:
        d_card_status: dict = super().to_json()
        d_card_status["s_user_id"] = self.s_user_id
        d_card_status["s_card_id"] = self.s_card_id
        d_card_status["s_insert_date"] = self.s_insert_date
        return d_card_status
