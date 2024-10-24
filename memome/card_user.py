from utils import generate_id
import repr_utils as ru
from memome_object import MemoMeObject


class CardUser(MemoMeObject):
    def __init__(self, s_user_name: str, s_user_pwd: str, s_obj_id):
        super().__init__(s_obj_id, "CardUser")
        self.s_user_name: str = s_user_name
        self.s_user_pwd: str = s_user_pwd

    def __str__(self) -> str:
        return ru.obj_to_str(self, "CardUser", 0)

    def to_json(self) -> dict:
        d_card_user: dict = super().to_json()
        d_card_user["s_user_name"] = self.s_user_name
        d_card_user["s_user_pwd"] = self.s_user_pwd
        return d_card_user

