"""A1 - 009"""
def scorecheck(mid : int,fin : int):
    """pass or fail"""
    score = mid + fin
    if score >= 50:
        return f"{score}\npass"
    return f"{score}\nfail"

print(scorecheck(int(input()),int(input())))
