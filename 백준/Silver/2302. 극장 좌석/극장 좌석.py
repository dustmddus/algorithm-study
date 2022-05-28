#좌석의 개수
n=int(input())
#고정석 개수
m=int(input())
fix=[0]
for i in range(m):
    fix.append(int(input()))
fix.append(n+1)
d=[1 for _ in range(45)]
d[1]=1
d[2]=2
for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]
result=1
for i in range(1,m+2):
    result*=d[fix[i]-fix[i-1]-1]
print(result)

