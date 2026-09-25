"""Color Code"""
r1, g1, b1 = map(int, input().split())

r2, g2, b2 = map(int, input().split())

r_mix = (r1 + r2) // 2
g_mix = (g1 + g2) // 2
b_mix = (b1 + b2) // 2

print(f"{r_mix} {g_mix} {b_mix}")
