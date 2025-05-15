"""A1 - 035"""
def sumsquare(n):
    """sum^2"""
    ruam = 0
    for i in range(1,n+1):
        ruam += i**2
    print(ruam)

sumsquare(int(input()))
