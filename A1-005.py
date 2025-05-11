"""A1 - 005"""
def season(month,date):
    """4 Season"""
    if ((1 <= month <= 3) and not(month == 3 and date >= 21)) or (month == 12 and date >= 21):
        return "winter"
    elif (4 <= month <= 6) and not(month == 6 and date >= 21) or (month == 3 and date >= 21):
        return "spring"
    elif (7 <= month <= 9) and not(month == 9 and date >= 21) or (month == 6 and date >= 21):
        return "summer"
    return "fall"

print(season(int(input()),int(input())))
    