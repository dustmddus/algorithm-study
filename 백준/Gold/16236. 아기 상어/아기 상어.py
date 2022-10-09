from collections import deque

n=int(input())

board=[list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j]==9:
            nx,ny=i,j
            board[i][j]=0
            break


size=2
dx=[1,0,-1,0]
dy=[0,1,0,-1]
total=0
eat=0
while True:
    q=deque()
    q.append([nx,ny,0])
    visited=[[False]*n for _ in range(n)]
    visited[nx][ny]=True
    flag=1e9
    fish=[]
    while q:
        x,y,count=q.popleft()
        if count>flag:
            break
        for dir in range(4):
            nx=x+dx[dir]
            ny=y+dy[dir]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if board[nx][ny]>size or visited[nx][ny]:
                continue
            if board[nx][ny]!=0 and board[nx][ny]<size:
                fish.append([nx,ny,count+1])
                flag=count
            q.append([nx,ny,count+1])
            visited[nx][ny]=True
    if len(fish)>0:
        fish.sort()
        x,y,time=fish[0][0],fish[0][1],fish[0][2]
        board[x][y]=0
        eat+=1
        if size==eat:
            size+=1
            eat=0
        nx=x
        ny=y
        total+=time
    else:
        break
print(total)
