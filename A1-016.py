"""A1 - 016"""
def checkerID(stdID):
    """stdID"""
    if stdID[2] in ('1','6') and stdID[3] in ('1','6'):
        return "yes"
    return "no"

print(checkerID(input()))
