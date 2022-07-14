import numpy as np

class Date:
    def __init__(self):
        self.date_str(input(f"Enter today's date (through ' - '): "))

    @classmethod
    def date_str(cls, date_int):
        print(date_int.split('-'))

    @staticmethod
    def get_date(cls, date_int):
        splits = np.array_split(date_int, 3)
        for array in splits:
            print(list(array))


the_date = Date()
print(Date.get_date(the_date(1)))
