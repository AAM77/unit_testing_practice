
from typing import List




person_list: List[tuple] = [
    ("John Doe", "9873459870"),
    ("Jane Doe", "1935673212"),
    ("John Smith", "987"),
]

def create_phonebook(people: list) -> dict:
    phonebook: dict = {}

    for person, number in people:
        if any(number in phone_number for phone_number in phonebook.values()):
            continue
        phonebook[person] = number

    breakpoint()
    return phonebook

