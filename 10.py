# Функція пори року із виключеннями

def pora_roku(n):

    try:

        if n < 0 or n > 12:
            raise ValueError("Argument must be a number between 1 and 12.")
        if n == 1 or n == 2 or n == 12:
            return "Winter"
        elif n == 3 or n == 4 or n == 5:
            return "Spring"
        elif n == 6 or n == 7 or n == 8:
            return "Summer"
        elif n == 9 or n == 10 or n == 11:
            return "Autumn"

    except TypeError as msg:
        print("Only integers are allowed")


#Функція списку унікальних чисел із виключеннями

def u_numbers(spis):

    if not type(spis) is list:
        raise TypeError("Only list are allowed")
    for i in spis:
        if not type(i) is int:
            raise ValueError("List elements must be numbers")

    res = set(spis)

    if len(spis) == len(res):
        print("The list contains unique numbers")
    else:
        print("The list contains non-unique numbers")

#Клас виключення
class MyError(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):

        if self.msg:
            return "MyError, {0}".format(self.msg)
        else:
            return "MyError has been raised"


raise MyError("Something went wrong")






