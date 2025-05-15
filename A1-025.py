"""A1 - 025"""
def cards(type: str):
    """cards"""
    num = {"A":"ace","J":"jack","Q":"queen","K":"king"}
    sign = {"D":"diamonds","H":"hearts","S":"spades","C":"clubs"}
    if type[:len(type) - 1].isnumeric() :
        return f"{type[:len(type) - 1]} of {sign[type[-1].upper()]}"
    return f"{num[type[:len(type) - 1]]} of {sign[type[-1].upper()]}"

print(cards(input()))
