"""A1 - 019"""
def ats(n1,n2,n3):
    """all the same"""
    if n1 == n2 == n3:
        return "all the same"
    elif n1 != n2 and n1 != n3 and n2 != n3:
        return "all different"
    return "neither"

print(ats(int(input()),int(input()),int(input())))
