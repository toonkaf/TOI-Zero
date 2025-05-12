"""A1 - 006"""
def modmai(num1 : int, num2 : int):
    """yes or no"""
    if (num1 % num2):
        return "no"
    return "yes"

print(modmai(int(input()),int(input())))
