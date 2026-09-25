data = []
while True:
    try:
        line = input().split()
        for x in line:
            data.append(int(x))
    except EOFError:
        break

if data:
    l = data[0]
    n = data[1]

    if n <= 0:
        print(0)
    else:
        # Binary search for the smallest band k where (k * (k + 1) // 2) * l >= n
        low = 1
        high = 2 * (10 ** 9)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            # Total capacity up to band 'mid' using integer division
            total_capacity = (mid * (mid + 1) // 2) * l
            
            if total_capacity >= n:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        print(ans)