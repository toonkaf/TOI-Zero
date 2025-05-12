"""A1 - 008"""
def idcheck(id: str):
    if len(id) == 13:
        return "yes"
    return "no"

print(idcheck(input()))
