"""A1 - 039"""
def factorial(num):
    """1 * 2 * 3 * ... * n-1 * n"""
    kept = 1
    for i in range(2,num+1):
        kept *= i
    print(kept)

factorial(int(input()))
