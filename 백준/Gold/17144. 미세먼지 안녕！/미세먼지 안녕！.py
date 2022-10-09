r,c,t=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(r)]

for i in range(r):
    if board[i][0] == -1:
        front = i
        back=i+1
        break

def spread():
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    temp=[[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j]>0:
                value=0
                for dir in range(4):
                    nx=i+dx[dir]
                    ny=j+dy[dir]
                    if 0<=nx<r and 0<=ny<c and board[nx][ny]!=-1:
                        temp[nx][ny]+=board[i][j]//5
                        value+=board[i][j]//5
                board[i][j]-=value
    for i in range(r):
        for j in range(c):
            board[i][j]+=temp[i][j]

def air_up():
    dx=[0,-1,0,1]
    dy=[1,0,-1,0]   #동, 북, 서, 남
    direct=0
    x,y=front,1
    before=0
    while True:
        nx=x+dx[direct]
        ny=y+dy[direct]
        if x==front and y==0:
            break
        if nx<0 or nx>=r or ny<0 or ny>=c:
            direct+=1
            continue
        board[x][y],before=before,board[x][y]
        x,y=nx,ny
def air_down():
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    direct=0
    x,y=back,1
    before=0
    while True:
        nx=x+dx[direct]
        ny=y+dy[direct]
        if x==back and y==0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        board[x][y],before=before,board[x][y]
        x,y=nx,ny

for _ in range(t):
    spread()
    air_up()
    air_down()

result=0

for i in range(r):
    for j in range(c):
        if board[i][j]>0:
            result+=board[i][j]
print(result)

