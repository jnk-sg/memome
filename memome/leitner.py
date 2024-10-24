from utils import generate_id
import repr_utils as ru
from memome_object import MemoMeObject
from box import Box


class Leitner(MemoMeObject):
    def __init__(self, s_title: str, s_obj_id):
        super().__init__(s_obj_id, "Leitner")
        self.s_title: str = s_title
        self.d_boxes: dict = {}

    def __str__(self) -> str:
        return ru.obj_to_str(self, "Leitner", 0)

    def add_box(self, new_box: Box) -> None:
        self.d_boxes[new_box.s_obj_id] = new_box

    def remove_box(self, s_obj_id: str) -> None:
        self.d_boxes.pop(s_obj_id)

    def update_boxs_status(self, s_date_time: str):
        for key in self.d_boxes.keys():
            c_box: Box = self.d_boxes[key]
            c_box.update_cards_status(s_date_time)

    def to_json(self) -> dict:
        d_leitner: dict = super().to_json()
        d_leitner["s_title"] = self.s_title
        d_leitner["d_boxes"] = {}
        for key in self.d_boxes.keys():
            box: Box = self.d_boxes[key]
            d_leitner["d_boxes"][box.s_obj_id] = box.to_json()
        return d_leitner
