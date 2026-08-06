"""This program is made to calculate the temperature"""
def main():
    """The program of temperature calculation"""
    #I mean this is probably my preferred way of coding
    temp = float(input())
    initemp = input()
    wanttemp = input()
    if initemp == "C":
        celsius = temp
    elif initemp == "K":
        celsius = temp - 273.15
    elif initemp == "F":
        celsius = (temp - 32) * 5 / 9
    else:
        celsius = (temp * 5 / 9) - 273.15
    #Seperate the Line
    if wanttemp == "C":
        answer = celsius
    elif wanttemp == "K":
        answer = celsius + 273.15
    elif wanttemp == "F":
        answer = (celsius * 9 / 5) + 32
    else:
        answer = (celsius + 273.15) * 9 / 5
    print(f"{answer:.2f}")
main()
