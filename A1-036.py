"""A1 - 036"""
def divten(n: str):
    """/10"""
    n = int(f"{n[:-1]}0")
    for i in range(n,-1,-10):
        print(i,end=" ")

divten(input())
