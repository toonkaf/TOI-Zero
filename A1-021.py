"""A1 - 021"""
def leap(year):
    """leap year"""
    if (year % 4) or (year > 1582 and not (year % 100) and year % 400):
        return "no"
    return "yes"

print(leap(int(input())))
