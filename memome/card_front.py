from utils import generate_id
import repr_utils as ru


class CardFront:
    def __init__(self, s_front: str):
        self.s_front: str = s_front

    def __str__(self) -> str:
        return ru.obj_to_str(self, "CardFront", 0)

    def to_json(self) -> dict:
        return {
            "s_front": self.s_front,
        }
