"""A1 - 004"""
def checker(ex : int, mid : int, fin : int):
    """pass or fail"""
    if (ex >= 5 and mid >= 20 and fin >= 25):
        return "pass"
    return "fail"

print(checker(int(input()),int(input()),int(input())))
