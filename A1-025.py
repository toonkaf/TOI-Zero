"""A1 - 025"""
def cards(types: str):
    """cards"""
    num = {"A":"ace","J":"jack","Q":"queen","K":"king"}
    sign = {"D":"diamonds","H":"hearts","S":"spades","C":"clubs"}
    if types[:len(types) - 1].isnumeric() :
        return f"{types[:len(types) - 1]} of {sign[types[-1].upper()]}"
    return f"{num[types[:len(types) - 1]]} of {sign[types[-1].upper()]}"

print(cards(input()))
