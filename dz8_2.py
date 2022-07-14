class ExceptionOfDivision(Exception):
    pass

class Division:
    def division(self, num_1, num_2):
        if num_2 != 0:
            print(self.division(input(f"Enter two numbers and you will see result of it's division {num_1, num_2}: {num_1 / num_2}")))
        else:
            raise ExceptionOfDivision


on_null = Division()
try:
    on_null.division(10, 0)
except ExceptionOfDivision as err:
    print("You can't divide on nul!!!")
