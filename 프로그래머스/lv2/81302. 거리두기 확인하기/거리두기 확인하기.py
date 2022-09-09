from collections import deque
def bfs(board):
    start=[]
    for i in range(5):
        for j in range(5):
            if board[i][j]=='P':
                start.append([i,j])
    for s in start:
        q=deque([s])
        visited=[[0]*5 for _ in range(5)]
        distance=[[0]*5 for _ in range(5)]
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        while q:
            x,y=q.popleft()
            visited[x][y]=1
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<5 and 0<=ny<5 and visited[nx][ny]==0:
                    if board[nx][ny]=='O':
                        q.append([nx,ny])
                        visited[nx][ny]=1
                        distance[nx][ny]=distance[x][y]+1
                    if board[nx][ny]=='P' and distance[x][y]<=1:
                        return 0
    return 1
    

def solution(places):
    answer=[]
    for i in places:
        answer.append(bfs(i))
    return answer