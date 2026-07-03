"""ค่าใช้จ่าย"""
def main():
    price = float(input())
    service = price/10
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000
    novat =  service + price
    vat = (novat*7)/100
    total = novat + vat
    print(f"{total:.2f}")
main()