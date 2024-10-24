class Box:
    def __init__(self, s_title: str, i_review_frequency: int, s_box_id: str = ""):
        self.s_box_id: str = generate_id("BOX_", "_ID") if not s_box_id else s_box_id
        self.s_title: str = s_title
        self.i_review_frequency: int = i_review_frequency
        self.d_cards_status: dict = {}

    def __str__(self) -> str:
        return ru.obj_to_str(self, "Box", 0)

    def add_card_status(self, new_card_status: CardStatus) -> None:
        self.d_cards_status[new_card_status.s_card_id] = new_card_status

    def remove_card_status(self, s_id: str) -> None:
        self.d_cards_status.pop(s_id)

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
        d_box = {
            "s_box_id": self.s_box_id,
            "s_title": self.s_title,
            "i_review_frequency": self.i_review_frequency,
            "d_cards_status": {}
        }
        for key in self.d_cards_status.keys():
            card: CardStatus = self.d_cards_status[key]
            d_box["d_cards_status"][card.s_status_id] = card.to_json()
        return d_box


