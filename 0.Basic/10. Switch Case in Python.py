# switch case statement

def day1():
    return "Monday"


def day2():
    return "Tuesday"


def day3():
    return "Wednesday"


def day4():
    return "Thursday"

def day5():
    return "Friday"


def day6():
    return "Saturday"


def day7():
    return "Sunday"

def default():
    return "Incorrect Day"

switcher = {
        1: day1,
        2: day2,
        3: day3,
        4: day4,
        5: day5,
        6: day6,
        7: day7,
    }

def switch(DayWeek):
        return switcher.get(DayWeek, default)()

x = int(input("Please Enter Day number 1 to 7 : "))
print(switch(x))