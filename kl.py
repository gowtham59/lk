import math
a1,a21=map(int,input().split())
c3=[]
b4=list(map(int,input().split()))
for i in range(0,a21):
    l,h=map(int,input().split())
    c3.append([l,h])
for i in c3:
    d=i[0]-1
    e=i[1]-1
    print(math.gcd(b4[d],b4[e]))
