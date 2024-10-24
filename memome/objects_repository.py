import json
import repr_utils as ru


class ObjectsRepository:
    def __init__(self, s_repository_file_path_name: str):
        self.s_repository_file_path_name: str= s_repository_file_path_name
        self._items: dict = {}

    def __str__(self) -> str:
        return ru.obj_to_str(self, "ObjectsRepository", 0)

    def add(self, s_obj_id: str, item: object) -> None:
        """Aggiunge un oggetto al repository."""
        if s_obj_id in self._items:
            raise ValueError(f"Un oggetto con chiave '{s_obj_id}' esiste già.")
        self._items[s_obj_id] = item

    def add_from_json(self, s_obj_id: str, d_obj_data: dict) -> None:
        """ Dato un dizionario nel quale esiste una chiave s_obj_type il cui valore è il nome del tipo di oggetto da creare
            la funzione prende dal dizionario i nomi dei parametri e i corrispettivi valore
            le concatena in una unica stringa ci aggiunge il come della classe all'inizio e poi chiama eval per la valutazione

            esmpio: d_obj_data = {'s_obj_type': 'CardUser', 's_user_id': 'USER_a5fqtt9zimbfzp8o_ID', 's_user_name': 'Pippo', 's_user_pwd': 'pippo_pwd'}
            s_constructor_params == s_user_id='USER_pevgciqro12vkagi_ID', s_user_name='Pippo', s_user_pwd='pippo_pwd'
            f"{s_class_type_name}({s_constructor_params})" == CardUser(s_user_id='USER_cngp67iroa3rj625_ID', s_user_name='Pippo', s_user_pwd='pippo_pwd')
        """
        s_class_type_name = d_obj_data.pop('s_obj_type')
        s_constructor_params = ', '.join(f"{k}='{v}'" for k, v in d_obj_data.items())
        c_class_instance = eval(f"{s_class_type_name}({s_constructor_params})")
        self._items[s_obj_id] = c_class_instance

    def remove(self, s_obj_id: str) -> None:
        """Rimuove un oggetto dal repository usando la chiave."""
        if s_obj_id not in self._items:
            raise KeyError(f"Nessun oggetto trovato con chiave '{s_obj_id}'.")
        del self._items[s_obj_id]

    def update(self, s_obj_id, item: object) -> None:
        """Aggiorna un oggetto esistente nel repository."""
        if s_obj_id not in self._items:
            raise KeyError(f"Nessun oggetto trovato con chiave '{s_obj_id}'.")
        self._items[s_obj_id] = item

    def get(self, s_obj_id: str) -> object:
        """Recupera un oggetto dal repository usando la chiave."""
        return self._items.get(s_obj_id, None)

    def get_all(self) -> list:
        """Ritorna tutti gli oggetti nel repository."""
        return list(self._items.values())

    def exists(self, s_obj_id: str) -> bool:
        """Controlla se un oggetto con una data chiave esiste nel repository."""
        return s_obj_id in self._items

    def to_json(self) -> dict:
        d_json_repr: dict = {}
        for key in self._items.keys():
            d_json_repr[key] = self._items[key].to_json()
        return d_json_repr

    def load_repository(self) -> None:
        pass

    def save_repository(self) -> None:
        with open(self.s_repository_file_path_name, "w") as data_file:
            json.dump(self.to_json(), data_file)


if __name__ == "__main__":
    # Esempio di utilizzo
    repository = ObjectsRepository()

    # Aggiungere un oggetto
    repository.add("1", {"nome": "oggetto1"})
    repository.add("2", {"nome": "oggetto2"})

    # Recuperare un oggetto
    oggetto = repository.get("1")
    print(oggetto)  # Output: {'nome': 'oggetto1'}

    # Aggiornare un oggetto
    repository.update("1", {"nome": "oggetto1_aggiornato"})

    # Verificare se un oggetto esiste
    esiste = repository.exists("1")  # Output: True

    # Rimuovere un oggetto
    repository.remove("2")

    # Recuperare tutti gli oggetti
    tutti = repository.get_all()
    print(list(tutti))  # Output: [{'nome': 'oggetto1_aggiornato'}]
