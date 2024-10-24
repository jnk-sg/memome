import repr_utils as ru


class ObjectsRepository:
    def __init__(self, s_repository_file_path_name: str):
        self.s_repository_file_path_name: s_repository_file_path_name
        self._items = {}

    def __str__(self) -> str:
        return ru.obj_to_str(self, "ObjectsRepository", 0)

    def add(self, s_obj_id: str, item: object) -> None:
        """Aggiunge un oggetto al repository."""
        if s_obj_id in self._items:
            raise ValueError(f"Un oggetto con chiave '{s_obj_id}' esiste già.")
        self._items[s_obj_id] = item

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
        """
        # creazione dinamica di una classe

        dati: dict = u0.to_json()
        pprint.pprint(dati)

        # Passo 1: Estrai il nome della classe dal dizionario
        nome_classe = dati.pop('s_obj_type')  # 'CardUser'

        # Passo 2: Usa eval per creare l'istanza dinamicamente
        # Unisci i parametri del dizionario in una stringa da passare a eval
        params = ', '.join(f"{k}='{v}'" for k, v in dati.items())

        # Passo 3: Crea dinamicamente l'istanza con eval()
        istanza = eval(f"{nome_classe}({params})")

        # Verifica il risultato
        print(istanza)  # Output: CardUser(s_user_id=USER_cy511y06gtnrxtoq_ID, s_user_name=Ste, s_user_pwd=pwd_ste)
        """
        pass

    def save_repository(self) -> None:
        pass




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
