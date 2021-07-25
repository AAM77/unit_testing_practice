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
    new_phonebook: object = phonebook.PhoneBook()
    new_phonebook.add(name="John Doe", number="1234567890")
    assert isinstance(new_phonebook, phonebook.PhoneBook)

def test_add_multiple():
    people: list = [
        ("f1 l1", "198724"),
        ("f2 l2", "298734")
    ]

    new_phonebook: object = phonebook.PhoneBook()
    assert new_phonebook.add_multiple(people) == {
                                                    "f1 l1": "198724",
                                                    "f2 l2": "298734"
                                                }

def test_phonebook_lookup():
    new_phonebook: object = phonebook.PhoneBook()
    new_phonebook.add(name="John Doe", number="1234567890")
    number = new_phonebook.lookup(name="John Doe")
    assert number == "1234567890"

def test_missing_name():
    new_phonebook: object = phonebook.PhoneBook()
    new_phonebook.add(name="John Doe", number="1234567890")
    with pytest.raises(Exception):
        assert new_phonebook.lookup(name="Jane")

def test_phonebook_consistency():
    is_consistent: bool = True
    people: list = [
        ("f1 l1", "198724"),
        ("f2 l2", "298734"),
        ("f3 l3", "198"),
        ("f4 l4", "298"),
    ]

    new_phonebook: object = phonebook.PhoneBook()
    new_phonebook.add_multiple(people)

    for i, number in enumerate(new_phonebook.numbers.values()):
        for j, prefix in enumerate(new_phonebook.numbers.values()):
            if i != j and prefix in number:
                is_consistent = False
                break

    assert is_consistent == True, "No number should be the prefix of another."