"""
    Questo piccolo modulo è scritto solo per svincolare il programma principale dalla gestione del tempo fatta con PySide6
    Se un giorno voglio cambiare libreria per la gestione del tempo basta che cambi questo modulo e non il programma principale.
"""

from PySide6.QtCore import QDateTime

DATE_TIME_FORMAT = "yyyy-MM-dd - HH:mm:ss"


def delta_hours(s_first_date: str, s_second_date: str) -> int:
    """Dati due momenti temporali fatti da data e ora restituisce il numero di ore che esiste tra questi due momenti"""
    first_date = QDateTime.fromString(s_first_date, DATE_TIME_FORMAT)
    second_date = QDateTime.fromString(s_second_date, DATE_TIME_FORMAT)
    return int(first_date.secsTo(second_date) / 3600)


def delta_days(s_first_date: str, s_second_date: str) -> int:
    """Dati due momenti temporali fatti da data e ora restituisce il numero di giorni che esisteno tra questi due momenti"""
    first_date = QDateTime.fromString(s_first_date, DATE_TIME_FORMAT)
    second_date = QDateTime.fromString(s_second_date, DATE_TIME_FORMAT)
    return int(first_date.secsTo(second_date) / 3600 / 24)


def now_date_time() -> str:
    return QDateTime.currentDateTime().toString(DATE_TIME_FORMAT)


if __name__ == "__main__":
    today = QDateTime.currentDateTime()
    tomorrow = QDateTime(2024, 10, 24, 19, 0, 0)

    print(delta_hours(today.toString(DATE_TIME_FORMAT), tomorrow.toString(DATE_TIME_FORMAT)))
    print(delta_days(today.toString(DATE_TIME_FORMAT), tomorrow.toString(DATE_TIME_FORMAT)))

    print(delta_days("2024-10-22 - 22:00:00", "2024-10-23 - 22:00:00"))
    print(delta_hours("2024-10-22 - 22:00:00", "2024-10-23 - 23:00:00"))

    print(now_date_time())