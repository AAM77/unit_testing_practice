import inspect
import pytest
import phonebook

def test_phonebook_exists():
    assert phonebook.PhoneBook

def test_phonebook_type():
    assert inspect.isclass(phonebook.PhoneBook)

def tests_phonebook_numbers_type():
    new_phonebook = phonebook.PhoneBook()
    assert type(new_phonebook.numbers) == dict

def test_phonebook_add():
    new_phonebook = phonebook.PhoneBook()
    new_phonebook.add(name="John Doe", number="1234567890")
    assert isinstance(new_phonebook, phonebook.PhoneBook)

def test_phonebook_lookup():
    new_phonebook = phonebook.PhoneBook()
    new_phonebook.add(name="John Doe", number="1234567890")
    number = new_phonebook.lookup(name="John Doe")
    assert number == "1234567890"

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