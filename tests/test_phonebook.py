import inspect
import pytest
import phonebook

@pytest.fixture
def phone_book():
    return phonebook.PhoneBook()

def test_phonebook_exists(phone_book: object):
    assert phone_book

def test_phonebook_type():
    assert inspect.isclass(phonebook.PhoneBook)

def tests_phonebook_numbers_type(phone_book: object):
    assert type(phone_book.numbers) == dict

def test_phonebook_add(phone_book: object):
    phone_book.add(name="John Doe", number="1234567890")
    assert isinstance(phone_book, phonebook.PhoneBook)

def test_add_multiple(phone_book: object):
    people: list = [
        ("f1 l1", "198724"),
        ("f2 l2", "298734")
    ]

    phone_book.add_multiple(people)

    assert phone_book.numbers == {
                                                    "f1 l1": "198724",
                                                    "f2 l2": "298734"
                                                }

def test_phonebook_lookup(phone_book: object):

    phone_book.add(name="John Doe", number="1234567890")
    number = phone_book.lookup(name="John Doe")
    assert number == "1234567890"

def test_missing_name(phone_book: object):
    phone_book.add(name="John Doe", number="1234567890")
    with pytest.raises(Exception):
        assert phone_book.lookup(name="Jane")

def test_is_consistent(phone_book):
    assert phone_book.is_consistent() == True

def test_is_not_consistent(phone_book):
    assert phone_book.is_consistent(consistency = False) == False

def test_phonebook_consistency_duplicate_prefix(phone_book: object):
    people: list = [
        ("f1 l1", "198724"),
        ("f2 l2", "298734"),
        ("f3 l3", "198"),
        ("f4 l4", "298"),
    ]

    phone_book.add_multiple(people)
    assert phone_book.is_consistent() == True, "No number should be a duplicate of another."

def test_phonebook_consistency_duplicate(phone_book: object):
    people: list = [
        ("f1 l1", "198724"),
        ("f2 l2", "298734"),
        ("f3 l3", "198724"),
        ("f4 l4", "298734"),
    ]

    phone_book.add_multiple(people)
    assert phone_book.is_consistent() == True, "No number should be a duplicate of another."

def test_phonebook_consistency_when_empty(phone_book: object):
    people: list = []
    phone_book.add_multiple(people)
    assert phone_book.is_consistent() == True, "No number should be a duplicate of another."