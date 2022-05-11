n=int(input())
s=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    idx=1
    for k in list(map(int,input().split())):
        s[i][idx]=k
        idx+=1
d=[[0]*(n+1) for _ in range(n+1)]
d[1][1]=s[1][1]

for i in range(2,n+1):
    for j in range(1,i+1):
        d[i][j]=max(d[i-1][j-1],d[i-1][j])+s[i][j]
print(max(d[n]))
        
             
