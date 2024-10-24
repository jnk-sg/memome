class ObjectsRepository:
    def __init__(self):
        self._items = {}

    def add(self, key, item):
        """Aggiunge un oggetto al repository."""
        if key in self._items:
            raise ValueError(f"Un oggetto con chiave '{key}' esiste già.")
        self._items[key] = item

    def remove(self, key):
        """Rimuove un oggetto dal repository usando la chiave."""
        if key not in self._items:
            raise KeyError(f"Nessun oggetto trovato con chiave '{key}'.")
        del self._items[key]

    def update(self, key, item):
        """Aggiorna un oggetto esistente nel repository."""
        if key not in self._items:
            raise KeyError(f"Nessun oggetto trovato con chiave '{key}'.")
        self._items[key] = item

    def get(self, key):
        """Recupera un oggetto dal repository usando la chiave."""
        return self._items.get(key, None)

    def get_all(self):
        """Ritorna tutti gli oggetti nel repository."""
        return self._items.values()

    def exists(self, key):
        """Controlla se un oggetto con una data chiave esiste nel repository."""
        return key in self._items


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
