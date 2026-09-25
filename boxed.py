"""Remaster Box"""
def main():
    """Polish Box"""
    W,L,M,N= map(int,input().split())
    s=[]
    for A in range(M,N+1):
        left = L % A
        area = W * left
        space = left // 1 * (W // A)
        waste = area - space * A
        s.append(waste)
    print(min(s))
main()
