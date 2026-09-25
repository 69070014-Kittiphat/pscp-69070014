"""Venom the Last Dance"""
def main():
    """Bahkrums"""
    seats = int(input())
    while seats > 0:
        try:
            line = input()
            if not line:
                break
        except EOFError:
            break
        xy = line.split()
        x = int(xy[0])
        y = int(xy[1])
        if x < 15:
            print(-1)
            continue
        if y > seats:
            print(-2)
            continue
        if 15 <= x <= 22:
            price_per_ticket = 150 * 0.8
        elif x >= 60:
            price_per_ticket = 150 * 0.5
        else:
            price_per_ticket = 150
        total_price = int(price_per_ticket * y)
        seats -= y
        print(f"{total_price} {seats}")
main()
