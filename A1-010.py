"""A1 - 010"""
def ticket(age: int,s: str):
    """20 - 50"""
    if age < 18 or s in ('s','S'):
        return 20
    return 50

print(ticket(int(input()),input()))
