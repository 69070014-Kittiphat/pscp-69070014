"""ไอพวกหน้าม้า RAHHHH"""
def main():
    """Check if a surprising vote is possible"""
    score = float(input())
    maximum = float(input())
    minimum = score - (2 * maximum)
    # เอาศูนย์ออก
    if minimum < 0:
        minimum = 0
    if maximum >= 2 and minimum < maximum - 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
