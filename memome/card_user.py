from utils import generate_id
import repr_utils as ru


class CardUser:
    def __init__(self, s_user_name: str, s_user_pwd: str, s_user_id: str = ""):
        self.s_user_id: str = generate_id("USER_", "_ID") if not s_user_id else s_user_id
        self.s_user_name: str = s_user_name
        self.s_user_pwd: str = s_user_pwd

    def __str__(self) -> str:
        return ru.obj_to_str(self, "CardUser", 0)

    def to_json(self) -> dict:
        return {
            "s_obj_type": "CardUser",
            "s_user_id": self.s_user_id,
            "s_user_name": self.s_user_name,
            "s_user_pwd": self.s_user_pwd
        }

    def from_json(self, d_json_dict: dict) -> None:
        self.s_user_id = d_json_dict.get("s_user_id", generate_id(""))
        self.s_user_name = d_json_dict.get("s_user_name", generate_id(""))
        self.s_user_pwd = d_json_dict.get("s_user_pwd", generate_id(""))


if __name__ == '__main__':
    u0 = CardUser("Pippo", "pippo_pwd")

