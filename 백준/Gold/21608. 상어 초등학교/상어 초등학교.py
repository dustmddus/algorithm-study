'''
학생의 순서를 정했고, 각 학생이 좋아하는 학생 4명도 조사했다.
정해진 순서대로 학생의 자리를 정하려고 한다.
한 칸에는 학생 한 명의 자리만 있을 수 있고,

좋아하는 학생이 인접한 칸에 가장 많은 자리로
인접 한 칸 중 비어있는 칸이 가장 많은 칸으로
행의 번호가 가장 작은 칸으로
열의 번호가 가장 작은 칸으로
'''
n=int(input())

board=[[0]*n for _ in range(n)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def like(arr):
    maxi=0
    result=[]
    for i in range(n):
        for j in range(n):
            cnt=0
            if board[i][j]==0:
                for dir in range(4):
                    nx=i+dx[dir]
                    ny=j+dy[dir]
                    if 0<=nx<n and 0<=ny<n and board[nx][ny] in arr:
                        cnt+=1
                if maxi < cnt:
                    result = []
                    result.append([i, j])
                    maxi = cnt
                elif maxi == cnt:
                    result.append([i, j])
    return result




def empty(temp):
    maxi=0
    result=[]
    for x,y in temp:
        cnt=0
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                cnt += 1
        if maxi < cnt:
            result = []
            result.append([x, y])
            maxi = cnt
        elif maxi == cnt:
            result.append([x, y])
    return result


store=[[] for _ in range(n**2+1)]
for _ in range(n**2):
    a,b,c,d,e=map(int,input().split())
    store[a]=[b,c,d,e]
    temp=like([b,c,d,e])
    if len(temp)==1:
        x,y=temp[0]
        board[x][y]=a
    else:
        result=empty(temp)
        if len(result)!=1:
            result.sort(key=lambda x: (x[0], x[1]))
        x, y = result[0]
        board[x][y]=a

total=0
for i in range(n):
    for j in range(n):
        cnt=0
        for dir in range(4):
            nx=i+dx[dir]
            ny=j+dy[dir]
            if 0<=nx<n and 0<=ny<n and board[nx][ny] in store[board[i][j]]:
                cnt+=1
        if cnt!=0:
            total+=10**(cnt-1)
print(total)
