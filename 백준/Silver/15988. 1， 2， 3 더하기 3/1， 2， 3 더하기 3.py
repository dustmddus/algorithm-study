t=int(input())
d=[1,2,4]
for i in range(t):
    n=int(input())
    for j in range(len(d),n):
        d.append((d[j-1]+d[j-2]+d[j-3])%1000000009)
    print(d[n-1])
