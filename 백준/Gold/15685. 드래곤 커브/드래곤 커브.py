n=int(input())

arr=[[0]*101 for _ in range(101)]

dx=[0,-1,0,1]
dy=[1,0,-1,0]

for _ in range(n):
    y,x,d,g=map(int,input().split())
    arr[x][y]=1
    move=[d]
    for _ in range(g):
        tmp = []
        for j in range(len(move)):
            tmp.append((move[-j-1]+1)%4)
        move.extend(tmp)

    for k in move:
        x+=dx[k]
        y+=dy[k]
        arr[x][y]=1

ans=0

for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            ans+=1
print(ans)