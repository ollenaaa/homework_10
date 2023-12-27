from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if self.is_valid_phone_number(value):
            super().__init__(value)
        else:
            raise ValueError

    def is_valid_phone_number(self, value):
        return value.isdigit() and len(value) == 10


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            phone = Phone(phone)
            self.phones.append(phone)
        except ValueError as err:
            print(f"Invalid phone number {phone}")

    def remove_phone(self, phone):
        for p in self.phones:
            if str(p) == str(phone):
                self.phones.remove(p)

    def edit_phone(self, phone, new_phone):
        for i in range(len(self.phones)):
            if str(self.phones[i]) == str(phone):
                try:
                    update_phone = Phone(new_phone)
                    self.phones[i] = update_phone
                    return True
                except ValueError as err:
                    print(f"Error updating phone: {err}")
                    return False

        raise ValueError(f"Phone {phone} not found in the record.")

    def find_phone(self, phone):
        for i in range(len(self.phones)):
            if str(self.phones[i]) == str(phone):
                return self.phones[i]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            print(f"{name} does not exist in dictionary")

    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
        else:
            print(f"{name} does not exist in dictionary")


john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("55555555555")

try:
    john_record.edit_phone("5555575555", "77777777777")
except ValueError as err:
    print(err)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")

book = AddressBook()
book.add_record(john_record)
book.add_record(jane_record)

book.delete('jane')

for name, record in book.data.items():
    print(record)
