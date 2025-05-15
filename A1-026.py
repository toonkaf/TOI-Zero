"""A1 - 026"""
def evod():
    """Even Odd"""
    ev = 0
    od = 0
    for _ in range(3):
        kept = int(input())
        if kept % 2:
            od += 1
        else:
            ev += 1
    return f"even {ev}\nodd {od}"

print(evod())
