"""Electricity Bill"""
units = int(input())

used = units
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

vat = base * 0.07
ft = units * 0.50

total = base + vat + ft

print(f"{total:.1f}")
