"Big Frame"
lines = [input() for _ in range(5)]
max_len = max(len(line) for line in lines)
print("*" * (max_len + 4))
for line in lines:
    print(f"* {line.ljust(max_len)} *")
print("*" * (max_len + 4))
