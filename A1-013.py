"""A1 - 013"""
def safelock(char,digit):
    """safe"""
    if char != "H" and digit != "4567":
        return "safe locked"
    elif char != "H" and digit == "4567":
        return "safe locked - change char"
    elif char == "H" and digit != "4567":
        return "safe locked - change digit"
    return "safe unlocked"

print(safelock(input(),input()))
