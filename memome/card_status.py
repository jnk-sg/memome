from utils import generate_id
import repr_utils as ru


class CardStatus:
    def __init__(self, s_user_id: str, s_card_id: str, s_insert_date: str, s_status_id: str = ""):
        self.s_status_id: str = generate_id("STATUS_", "_ID") if not s_status_id else s_status_id
        self.s_user_id: str = s_user_id
        self.s_card_id: str = s_card_id
        self.s_insert_date: str = s_insert_date

    def __str__(self) -> str:
        return ru.obj_to_str(self, "CardStatus", 0)

    def to_json(self) -> dict:
        return {
            "s_card_status_id": self.s_status_id,
            "s_user_id": self.s_user_id,
            "s_card_id": self.s_card_id,
            "s_insert_date": self.s_insert_date,
        }


