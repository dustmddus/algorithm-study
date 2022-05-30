'''
빙산의 각 부분별 높이 정보는 배열의 각 칸에 양의 정수로 저장됨. 빙산 이외의
바다에 해당되는 칸에는 0이 저장된다.
빙산의 높이는 그 칸에 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼
줄어든다. 단 0보다 줄어들지는 않는다. 한 덩어리의 빙산이 두 덩어리 이상으로
분리되는 최초의 시간을 구하는 프로그램을 구하라.
'''
import sys
import collections
input=sys.stdin.readline
#행, 열
n,m=map(int,input().split())
#1년이 지날때마다 몇개의 덩어리가 있는지 check.

arr=[[]for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
global vis

for i in range(n):
    x=list(map(int,input().split()))
    arr[i]=x


def bfs(a,b):
    queue=collections.deque()
    queue.append([a,b])
    vis[a][b]=1
    while queue:
        a,b=queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if nx<0 or nx>n or ny<0 or ny>m:
                continue
            if arr[nx][ny]==0 or vis[nx][ny]==1:
                continue
            queue.append([nx,ny])
            vis[nx][ny]=1
    return 1

def check(arr):
    global vis
    vis=[[0]*m for _ in range(n)]
    tot=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0 or vis[i][j]==1:
                continue
            tot+=bfs(i,j)
    return tot
tot=0
while True:
    cnt_ice=0
    tmp=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            cnt=0
            if arr[i][j]!=0:
                cnt_ice+=1
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if arr[nx][ny]==0:
                        cnt+=1
                tmp[i][j]=cnt
    if cnt_ice==0:
        print(0)
        break
    for i in range(n):
        for j in range(m):
            if arr[i][j]-tmp[i][j]>=0:
                arr[i][j]-=tmp[i][j]
            else:
                arr[i][j]=0
    tot+=1
    
    if check(arr)>=2:
    
        print(tot)
        break
    

    
