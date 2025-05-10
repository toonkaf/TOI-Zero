"""A1 - 002"""
def exchange(money):
    """10 5 2 1"""
    ten ,left = divmod(money,10)
    money -= ten*10
    five ,left = divmod(money,5)
    money -= five*5
    two ,one = divmod(money,2)
    print(f"10 = {ten}\n5 = {five}\n2 = {two}\n1 = {one}")

exchange(int(input()))
