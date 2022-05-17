t=int(input())
d=[0]*100
d[0]=1
d[1]=1
d[2]=1
for i in range(3,100):
    d[i]=d[i-2]+d[i-3]

for i in range(t):
    n=int(input())
    print(d[n-1])
