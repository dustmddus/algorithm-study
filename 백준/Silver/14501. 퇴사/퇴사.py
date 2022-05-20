n=int(input())
t=[0]*20
p=[0]*20
d=[0]*20

for i in range(1,n+1):
    t[i],p[i]=map(int,input().split())

for i in range(1,n+1):
    d[i]=max(d[i-1],d[i])
    if(i+t[i]-1<=n):
        d[i+t[i]]=max(d[i+t[i]],d[i]+p[i])
print(max(d[n],d[n+1]))
