from memome.utils import repr_utils as ru, date_time_utils as dtu
from base_obj import BaseObj
from card_state import CardState
from card_status import CardStatus


class Box(BaseObj):
    def __init__(self, s_title: str, i_review_frequency: int, s_obj_id: str):
        super().__init__(s_obj_id, "Box")
        self.s_title: str = s_title
        self.i_review_frequency: int = i_review_frequency
        self.d_cards_status: dict = {}

    def __str__(self) -> str:
        return ru.obj_to_str(self, "Box", 0)

    def add_card_status(self, new_card_status: CardStatus) -> None:
        self.d_cards_status[new_card_status.s_card_id] = new_card_status

    def remove_card_status(self, s_card_status_id: str) -> CardStatus:
        return self.d_cards_status.pop(s_card_status_id)

    def get_cards_status(self, s_user_id: str) -> list:
        l_cards_status = []
        for key in self.d_cards_status.keys():
            c_status: CardStatus = self.d_cards_status[key]
            if c_status.s_user_id == s_user_id:
                l_cards_status.append(c_status)
        return l_cards_status

    def get_cards_status_with_state(self, s_user_id: str, e_state: CardState) -> list:
        l_cards_status: list = []
        for key in self.d_cards_status.keys():
            c_status: CardStatus = self.d_cards_status[key]
            if c_status.s_user_id == s_user_id and c_status.e_card_state == e_state:
                l_cards_status.append(c_status)
        return l_cards_status

    def update_cards_status(self, s_date_time: str):
        for key in self.d_cards_status.keys():
            c_status: CardStatus = self.d_cards_status[key]
            i_delta_time = dtu.delta_hours(s_date_time, c_status.s_insert_date)
            if i_delta_time < self.i_review_frequency:
                c_status.e_card_state = CardState.SLEEPING
            elif i_delta_time == self.i_review_frequency:
                c_status.e_card_state = CardState.TO_REVIEW
            elif i_delta_time > self.i_review_frequency:
                c_status.e_card_state = CardState.OUT_OF_DATE

    def to_json(self) -> dict:
        d_box: dict = super().to_json()
        d_box["s_title"] = self.s_title
        d_box["i_review_frequency"] = self.i_review_frequency
        d_box["s_title"] = self.s_title
        d_box["d_cards_status"] = {}
        for key in self.d_cards_status.keys():
            c_card_status: CardStatus = self.d_cards_status[key]
            d_box["d_cards_status"][c_card_status.s_obj_id] = c_card_status.to_json()
        return d_box


if __name__ == '__main__':
    from utils import generate_id

    cs0 = CardStatus(generate_id("USER_", "_ID"), generate_id("CARD_", "_ID"), dtu.now_date_time(), generate_id("CARD_STATUS", "_ID"))
    cs1 = CardStatus(generate_id("USER_", "_ID"), generate_id("CARD_", "_ID"), dtu.now_date_time(), generate_id("CARD_STATUS", "_ID"))
    cs2 = CardStatus(generate_id("USER_", "_ID"), generate_id("CARD_", "_ID"), dtu.now_date_time(), generate_id("CARD_STATUS", "_ID"))

    box = Box("Box Primo", 1, generate_id("BOX_"))
    box.add_card_status(cs0)
    box.add_card_status(cs1)

    print(box)
