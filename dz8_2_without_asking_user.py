class ExceptionOfDivision(Exception):
    pass

class Division:
    def division(self, num_1, num_2):
        if num_2 != 0:
            return num_1 / num_2
        else:
            raise ExceptionOfDivision


on_null = Division()
try:
    print(on_null.division(10, 5))
except ExceptionOfDivision as err:
    print("You can't divide on nul!!!")
