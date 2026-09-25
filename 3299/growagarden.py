"""Gag"""
def find_band(size_l, count_n):
    """flower"""
    total = 0
    band = 0
    while total < count_n:
        band += 1
        band_size = size_l * size_l * (band - 1) + size_l * (size_l + 1) // 2
        total += band_size
    return band


def main():
    """number"""
    tokens = []
    while len(tokens) < 2:
        tokens += input().split()
    size_l, count_n = int(tokens[0]), int(tokens[1])
    print(find_band(size_l, count_n))


if __name__ == "__main__":
    main()