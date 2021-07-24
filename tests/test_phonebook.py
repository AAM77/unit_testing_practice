import pytest
import phonebook

def test_create_phonebook_exists():
    assert phonebook.create_phonebook

def test_create_phonebook_result_type():
    assert type(phonebook.create_phonebook([("name1", "number1")])) == dict

def test_create_phonebook():
    people: list = [
        ("f1 l1", "198724"),
        ("f2 l2", "298734")
    ]

    assert phonebook.create_phonebook(people) == {
                                                    "f1 l1": "198724",
                                                    "f2 l2": "298734"
                                                }

def test_phonebook_consistency():
    is_consistent: bool = True
    people: list = [
        ("f1 l1", "198724"),
        ("f2 l2", "298734"),
        ("f3 l3", "198"),
        ("f4 l4", "298"),
    ]

    phone_book: dict = phonebook.create_phonebook(people)

    for i, number in enumerate(phone_book.values()):
        for j, prefix in enumerate(phone_book.values()):
            if i != j and prefix in number:
                is_consistent = False
                break

    assert is_consistent == True, "No number should be the prefix of another."