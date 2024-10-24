from utils import generate_id
import repr_utils as ru


class CardBack:
    def __init__(self, s_back: str):
        self.s_back: str = s_back

    def __str__(self) -> str:
        return ru.obj_to_str(self, "CardBack", 0)

    def to_json(self) -> dict:
        return {
            "s_back": self.s_back,
        }