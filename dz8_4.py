# import os
# print('os.name = ', os.name)
# import re
#
# string = 'This is simple test message for test'
# found = re.findall(r'test', string)
# print(found)
'''import random

lst = []
for _ in range(10):
    lst.append(random.randint(-10, 10))
'''
class OfficeEquipStock:
    pass


class OfficeEquipment:
    def __init__(self, model, sheets_in_day):
        self.model = model
        self.sheets_in_day = sheets_in_day

    def my_data(self):
        print(f'Hello, my model is {self.model} and I can do {self.sheets_in_day} sheets of documents in day!')

class Printer(OfficeEquipment):
    def __init__(self, model, sheets_in_day):
        super().__init__(model, sheets_in_day)

    def friend_p(self):
        print(f"so, I'm your office-friend, Printer 📇 ")


class Scanner(OfficeEquipment):
    def __init__(self, model, sheets_in_day):
        super().__init__(model, sheets_in_day)

    def friend_p(self):
        print(f"so, I'm your office-friend, Scanner  📃 📄 ")

class Xerox(OfficeEquipment):
    def __init__(self, model, sheets_in_day):
        super().__init__(model, sheets_in_day)

    def friend_p(self):
        print(f"so, I'm your office-friend, Xerox 📰 ")

printer_1 = Printer('Hewlett-Packard', 400)
printer_1.my_data()
printer_1.friend_p()
print()

printer_1 = Scanner('Epson', 800)
printer_1.my_data()
printer_1.friend_p()
print()

printer_1 = Xerox('Canon CanoScan', 580)
printer_1.my_data()
printer_1.friend_p()
