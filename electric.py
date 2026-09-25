"""Kashimo"""
from decimal import Decimal, ROUND_HALF_UP
N = int(input())

used = N
base = 0

if used > 200:
    base += (used - 200) * 15
    used = 200
if used > 100:
    base += (used - 100) * 12
    used = 100
if used > 50:
    base += (used - 50) * 10
    used = 50
if used > 10:
    base += (used - 10) * 7
    used = 10
if used > 0:
    base += used * 5
ft = N * 0.50

vat = base * 0.07

total = base + vat + ft

result = Decimal(str(total)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)

print(result)
