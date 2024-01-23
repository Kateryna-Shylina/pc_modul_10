from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        required = True
    

class Phone(Field):
    def __init__(self, value):    
        super().__init__(value)
        if self.check_phone() == False:
            raise ValueError
        required = False
        
    def check_phone(self):
        if len(self.value) == 10 and self.value.isdigit():
            return True
        else:
            return False


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        if phone.check_phone() == True:
            self.phones.append(phone)
        else:
            raise ValueError
        
    def edit_phone(self, old_phone, new_phone):   
        for phone in self.phones:
            if phone.value == old_phone:
                self.add_phone(new_phone)
                self.remove_phone(old_phone)                
                break
        else:
            raise ValueError
        
    def remove_phone(self, phone_number):
        index = -1
        for phone in self.phones:
            index += 1
            if phone.value == phone_number:
                break
        else:
            raise ValueError

        self.phones.pop(index)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        for key, record in self.data.items():
            if key == name:
                return record
        
    def delete(self, name):
        for key, record in self.data.items():
            if key == name:
                del self.data[name]
                break


if __name__ == '__main__':
# Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
