"""color"""
def main():
    color1=str(input())
    color2=str(input())
    if color1 == "Red":
        if color2=="Yellow":
            print("Orange")
        elif color2=="Blue":
            print("Violet")
        elif color2=="Red":
            print("Red")
        else:
            print("Error")
    elif color1=="Blue":
        if color2=="Yellow":
            print("Green")
        elif color2=="Red":
            print("Violet")
        elif color2=="Blue":
            print("Blue")
        else:
            print("Error")
    elif color1=="Yellow":
        if color2=="Red":
            print("Orange")
        elif color2=="Blue":
            print("Green")
        elif color2=="Yellow":
            print("Yellow")
        else:
            print("Error")
    else:
        print("Error")
main()