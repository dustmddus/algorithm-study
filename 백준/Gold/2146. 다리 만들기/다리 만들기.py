'''
한 섬과 다른 섬을 잇는 다리를 하나만 만들겠소. 다리를 가장 짧게 하여 돈을 아끼려
가장 짧은 다리를 하나 놓아 두 대륙을 연결하는 방법
일단 덩어리를 나눠야 한다.
길이는 두 좌표를 각각 빼서 거기서 1을 뺀다.
만약 0을 만난다면 해당 좌표
경계에 있는 것들을 기준으로 빼준다. 
'''
from collections import deque
n=int(input())
board=[]
vis=[[0]*n for _ in range(n)]
queue=deque()
dx=[1,0,-1,0]
dy=[0,1,0,-1]

for i in range(n):
    board.append(list(map(int,input().split())))

#덩어리 나누기
def bfs(i,j):
    queue.append((i,j))
    arr=[]
    vis[i][j]=1
    while queue:
        x,y=queue.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            
            #덩어리 경계 배열로 모으기
            if board[nx][ny]==0 and ((x,y) not in arr):
                arr.append((x,y))
                continue
            if board[nx][ny]==0 or vis[nx][ny]==1:
                continue
            vis[nx][ny]=1
            queue.append((nx,ny))
    return arr
tot=0
result=[]
for i in range(n):
    for j in range(n):
        if board[i][j]==1 and vis[i][j]==0:
            tot+=1
            result.append(bfs(i,j))


def dist(x,y):
    dis_arr=[]
    for i in range(len(result[x])):
        for j in range(len(result[y])):
            dis=abs(result[x][i][0]-result[y][j][0])+abs(result[x][i][1]-result[y][j][1])-1
            dis_arr.append(dis)
    return min(dis_arr)
    
    
#덩어리 경계끼리 빼줘서 거리 구하기

answer=[]
for i in range(tot):
    for j in range(i+1,tot):
        answer.append(dist(i,j))

print(min(answer))

