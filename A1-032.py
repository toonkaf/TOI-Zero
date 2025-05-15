"""A1 - 032"""
def dokjan(n:int):
    """n -> n-2 -> n-4"""
    for _ in range(3):
        if n <= 0:
            break
        print(n*"*")
        n = n-2

dokjan(int(input()))
