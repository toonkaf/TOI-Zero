"""A1 - 034"""
def minimum(n):
    """minimum"""
    kept = []
    for _ in range(n):
        kept.append(int(input()))
    return min(kept)

print(minimum(int(input())))
