"""A1 - 029"""
def co(word: str):
    """counts"""
    kept = 0
    for i in word:
        if i in ('a','e','i','o','u'):
            kept += 1
    return kept

print(co(input()))
