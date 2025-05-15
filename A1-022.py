"""A1 - 022"""
def zodiac(date,month):
    """Zodiac"""
    if (date >= 22 and month == 12) or (date <= 19 and month == 1):
        return "capricorn"
    if (date >= 20 and month == 1) or (date <= 18 and month == 2):
        return "aquarius"
    if (date >= 19 and month == 2) or (date <= 20 and month == 3):
        return "pisces"
    if (date >= 21 and month == 3) or (date <= 19 and month == 4):
        return "aries"
    if (date >= 20 and month == 4) or (date <= 20 and month == 5):
        return "taurus"
    if (date >= 21 and month == 5) or (date <= 21 and month == 6):
        return "gemini"
    if (date >= 22 and month == 6) or (date <= 22 and month == 7):
        return "cancer"
    if (date >= 23 and month == 7) or (date <= 22 and month == 8):
        return "leo"
    if (date >= 23 and month == 8) or (date <= 22 and month == 9):
        return "virgo"
    if (date >= 23 and month == 9) or (date <= 23 and month == 10):
        return "libra"
    if (date >= 24 and month == 10) or (date <= 21 and month == 11):
        return "scorpio"
    if (date >= 22 and month == 11) or (date <= 21 and month == 12):
        return "sagittarius"

print(zodiac(int(input()),int(input())))
