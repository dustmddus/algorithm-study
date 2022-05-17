n=int(input())
s=list(map(int,input().split()))
d=s[:]
for i in range(n):
    for j in range(i):
        if s[i]>s[j]:
            d[i]=max(d[i],d[j]+s[i])
print(max(d))
