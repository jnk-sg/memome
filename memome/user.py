from memome.utils import repr_utils as ru
from base_obj import BaseObj


class User(BaseObj):
    def __init__(self, s_user_name: str, s_user_pwd: str, s_obj_id):
        super().__init__(s_obj_id, "User")
        self.s_user_name: str = s_user_name
        self.s_user_pwd: str = s_user_pwd

    def __str__(self) -> str:
        return ru.obj_to_str(self, "User", 0)

    def to_json(self) -> dict:
        d_user: dict = super().to_json()
        d_user["s_user_name"] = self.s_user_name
        d_user["s_user_pwd"] = self.s_user_pwd
        return d_user

