"""This program is made to told the season, whether it's summer or whatevs"""
def main():
    """This is a function use to told season in a year"""
    month = int(input())
    day = int(input())
    if 1 <= month <= 3:
        season = "winter"
        if month == 3 and day >= 21:
            season = "spring"
            print(season)
        else:
            print(season)
    elif 4 <= month <= 6:
        season = "spring"
        if month == 6 and day >= 21:
            season = "summer"
            print(season)
        else:
            print(season)
    elif 7 <= month <= 9:
        season = "summer"
        if month == 9 and day >= 21:
            season = "fall"
            print(season)
        else:
            print(season)
    elif 10 <= month <= 12:
        season = "fall"
        if month == 12 and day >= 21:
            season = "winter"
            print(season)
        else:
            print(season)
main()
