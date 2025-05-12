"""A1 - 011"""
def theos(s):
    """AAABB -> 3A2B"""
    kept = 1
    final = ""
    for i in range(1,5):
        if s[i] != s[i-1]:
            final += f"{kept}{s[i-1]}"
            kept = 0
        kept += 1
    final += f"{kept}{s[i]}"
    print(final)

theos(input())
