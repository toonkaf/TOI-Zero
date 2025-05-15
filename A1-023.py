"""A1 - 023"""
def slg(degree , cf):
    """solid liquid gas"""
    if (degree <= 0 and cf in ('C','c')) or (degree <= 32 and cf in ('F','f')) :
        return 'solid'
    if (0 < degree < 100 and cf in ('C','c')) or (32 < degree < 212 and cf in ('F','f')) :
        return 'liquid'
    return 'gas'

print(slg(int(input()),input()))
