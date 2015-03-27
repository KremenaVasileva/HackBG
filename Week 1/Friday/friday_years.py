import calendar


def year_start(year):
    result = 1
    if year >= 2007:
        for i in range(2007, year):
            if calendar.isleap(i):
                result += 2
            else:
                result += 1
    else:
        for i in range(year, 2007):
            if calendar.isleap(i):
                result -= 2
            else:
                result -= 1
    return result % 7


def friday_years(start, end):
    count = 0
    for i in range(start, end + 1):
        if year_start(i) == 5 or (year_start(i) == 4 and calendar.isleap(i)):
            count += 1
    return count


print (friday_years(1000, 2000))
print (friday_years(1753, 2000))
print (friday_years(1990, 2015))
