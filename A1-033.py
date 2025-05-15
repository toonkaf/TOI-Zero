"""A1 - 033"""
def check(n):
    """loop check"""
    nub = 0
    for _ in range(n):
        kept = input()
        if kept in ('A','E','I','O','U'):
            nub += 1
    return nub

print(check(int(input())))
