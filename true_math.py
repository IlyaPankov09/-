import math
# first = int(input('Введите первое число:'))
# second = int(input('Введите второе число:'))
def divide(first, second):
    if first != 0 and second != 0:
        result = first / second
        return(result)
    else:
        try:
            result = first / second
            return result
        except ZeroDivisionError:
            result = math.inf
            return(result)
#divide(4, 0)


