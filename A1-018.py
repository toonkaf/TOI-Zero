"""A1 - 018"""
def roman(num):
    """roman num"""
    lst = ["I","II","III","IV","V","VI","VII","VIII","IX"]
    if not num or num > 9:
        return "Error : Out of range"
    if num < 0:
        return "Error : Please input positive number"
    return lst[num - 1]

print(roman(int(input())))
