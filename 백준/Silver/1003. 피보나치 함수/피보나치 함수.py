n=int(input())
d=[[0,0] for _ in range(41)]
d[0][0]=1
d[1][1]=1


for i in range(2,41):
    d[i][1]=d[i-1][1]+d[i-2][1]
    d[i][0]=d[i-1][0]+d[i-2][0]
for i in range(n):
    t=int(input())
    print(d[t][0],d[t][1])
    
