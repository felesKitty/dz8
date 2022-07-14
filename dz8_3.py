class ListOfNumbers:
    def if_only_numbers(self, numbers):
        if numbers.isdigit():
            numbers = 0
            try:
                while numbers != 'stop':
                    for N in map(int, input('For exit type "stop" \n''Enter numbers with spaces ').split()):
                        numbers += N
                        N.append(numbers)
                    print(numbers)
            except ValueError:
                print(numbers)
        else:
            raise IfOnlyNumbers

class IfOnlyNumbers(Exception):
    pass

list = ListOfNumbers()
try:
    print(list.if_only_numbers('2'))
except IfOnlyNumbers as err:
    print("It isn't only numbers here!")
