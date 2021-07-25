from typing import List


class PhoneBook():

    def __init__(self):
        self.numbers: dict = {}

    def add(self, name: str, number: str):
        self.numbers[name] = number

    def add_multiple(self, people: list) -> dict:

        for name, number in people:
            if any(number in phone_number for phone_number in self.numbers.values()):
                continue
            self.add(name=name, number=number)

        return self.numbers

    def lookup(self, name: str) -> str:
        return self.numbers[name]
