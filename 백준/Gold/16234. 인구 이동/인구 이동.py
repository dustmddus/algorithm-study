from collections import deque

n,l,r=map(int,input().split())

board=[]
for i in range(n):
    board.append(list(map(int,input().split())))

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(x,y):
    tmp=[]
    q=deque()
    q.append((x,y))
    tmp.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                if l<=abs(board[x][y]-board[nx][ny])<=r:
                    visited[nx][ny]=1
                    tmp.append((nx,ny))
                    q.append((nx,ny))
    return tmp

cnt=0
while True:
    flag=False
    visited=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                visited[i][j]=1
                country=bfs(i,j)
                total=0
                if len(country)>1:
                    flag=True
                    for x,y in country:
                        total+=board[x][y]
                    ttotal=total//len(country)
                    for x,y in country:
                        board[x][y]=ttotal

    if not flag:
        print(cnt)
        break
    cnt+=1