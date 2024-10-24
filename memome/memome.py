"""
Note:
    1 - in questo progetto al momento non ho voglia di gestire l'incapsulazione dei dati quindi niente getter o setter
"""

# TODO:
#   1 - creare un repository come fatto da chatgpt ma invece che di una stringa c'è l'oggetto
#   2 - nel module ru mettere il colore dei nomi delle variabili dei dati primiti simile a quello delle altre non proprio uguale ma simile in modo che ho subito a colpo d'occhio
#       quali sono i nomi delle variabili

import json

from memome.utils import repr_utils as ru

from leitner import Leitner
from user import User


class MemoMe:
    def __init__(self,s_repository_file_path_name: str):
        self.s_repository_file_path_name: str = s_repository_file_path_name
        self.l_leitner: Leitner = None
        self.l_user: User = None

    def __str__(self) -> str:
        return ru.obj_to_str(self, "MemoMe", 0)

    def to_json(self) -> dict:
        return {
            self.l_leitner.s_obj_id: self.l_leitner.to_json(),
            self.l_user.s_obj_id: self.l_user.to_json()
        }

    def load_repository(self) -> None:
        pass

    def save_repository(self) -> None:
        with open(self.s_repository_file_path_name, "w") as data_file:
            json.dump(self.to_json(), data_file)


if __name__ == "__main__":
    pass