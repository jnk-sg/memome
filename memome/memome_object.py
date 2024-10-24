import repr_utils as ru


class MemoMeObject:
    def __init__(self, s_obj_id: str, s_obj_type_name: str):
        self.s_obj_id: str = s_obj_id
        self.s_obj_type_name: str = s_obj_type_name

    def __str__(self) -> str:
        return ru.obj_to_str(self, "MemoMeObject", 0)

    def to_json(self) -> dict:
        return {
            "s_obj_id": self.s_obj_id,
            "s_obj_type_name": self.s_obj_type_name
        }
