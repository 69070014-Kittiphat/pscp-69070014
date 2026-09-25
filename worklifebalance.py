"""Inner Peace, Chicken Cheess"""
data = []
while True:
    try:
        line = input().split()
        for x in line:
            data.append(int(x))
    except EOFError:
        break

if data:
    n = data[0]
    hours = data[1:n+1]

    heavy = 0
    light = 0

    for h in hours:
        if h > 18:
            heavy += 1
        else:
            light += 1

    if light >= heavy:
        print(n)
    else:
        print(2 * heavy - 1)
