"""A1 - 038"""
def everyfive(num):
    """****X****X"""
    s = "****X"
    full , left = divmod(num,5)
    lefts = left*"*"
    return f"{full * s}{lefts}"

print(everyfive(int(input())))
