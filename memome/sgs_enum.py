class SGSEnum:
    _values = {}

    def __init__(self, name, valore):
        self.name = name
        self.value = valore
        self.__class__._values[name] = self

    @classmethod
    def values(cls):
        """Restituisce una lista di tutti i valori della pseudo-enumerazione."""
        return list(cls._values.values())

    @classmethod
    def names(cls):
        """Restituisce una lista di tutti i nomi degli attributi."""
        return list(cls._values.keys())

    def __repr__(self):
        return f"<{self.__class__.__name__}.{self.name}: {self.value}>"

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def from_value(cls, value):
        """Restituisce il membro dell'enum dato un valore."""
        for attrib in cls._values.values():
            if attrib.value == value:
                return attrib
        raise ValueError(f"Valore {value} non presente nella {cls.__name__}")


if __name__ == "__main__":
    # Creazione della pseudo-enumerazione
    class Colore(SGSEnum):
        ROSSO = SGSEnum("ROSSO", 1)
        VERDE = SGSEnum("VERDE", 2)
        BLU = SGSEnum("BLU", 3)


    # Utilizzo
    print(Colore.ROSSO)  # Output: ROSSO
    print(repr(Colore.ROSSO))  # Output: <SimulazioneEnum.ROSSO: 1>

    # Iterazione su tutti i valori
    for colore in Colore.values():
        print(f"Nome: {colore.name}, Valore: {colore.value}")

    # Accesso tramite valore
    print(Colore.from_value(2))  # Output: VERDE
