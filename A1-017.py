"""A1 - 017"""
def bday(y1,m1,d1,y2,m2,d2):
    """birthday"""
    if y2 > y1 or (y1 == y2 and m2 > m1) or (y1 == y2 and m2 == m1 and d2 > d1):
        return 1
    if y2 < y1 or (y1 == y2 and m2 < m1) or (y1 == y2 and m2 == m1 and d2 < d1):
        return 2
    return 0

print(bday(int(input()),int(input()),int(input()),int(input()),int(input()),int(input())))
