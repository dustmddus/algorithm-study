from collections import deque
n,m=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(n)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def combi(arr,n):
    result=[]
    if n==0:
        return [[]]
    for i in range(len(arr)):
        elem=arr[i]
        for rest in combi(arr[i+1:],n-1):
            result.append([elem]+rest)
    return result

def bfs(active):
    q=deque()
    result=0
    visited=[[-1]*n for _ in range(n)]
    for x,y in active:
        q.append((x,y))
        visited[x][y]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny]==0 and visited[nx][ny]==-1:
                    q.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1
                    result=max(result,visited[nx][ny])
                elif board[nx][ny]==2 and visited[nx][ny]==-1:
                    q.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1

    cnt=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==-1:
                cnt+=1

    if cnt!=wall:
        return 1e9
    return result

virus=[]
wall=0
for i in range(n):
    for j in range(n):
        if board[i][j]==2:
            virus.append((i,j))
        if board[i][j]==1:
            wall+=1

ans=1e9
for active in combi(virus,m):
    ans=min(ans,bfs(active))

if ans==1e9:
    print(-1)
else:
    print(ans)