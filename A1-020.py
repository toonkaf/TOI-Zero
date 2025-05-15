"""A1 - 020"""
def inde(n1,n2,n3):
    """increasing or decreasing"""
    if n1 < n2 < n3:
        return "increasing"
    elif n1 > n2 > n3:
        return "decreasing"
    return "neither"

print(inde(int(input()),int(input()),int(input())))
