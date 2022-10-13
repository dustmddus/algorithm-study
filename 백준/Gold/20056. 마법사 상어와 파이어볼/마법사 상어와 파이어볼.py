#nxn 격자 m개 파이어볼 발사 k번 명령
import copy

n,M,k=map(int,input().split())

board=[[[] for _ in range(n)] for _ in range(n)]


dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]



#모든 파이어불이 자신의 방향d 만큼 속력 s 칸 만큼 이동한다.
def move():
    global board
    tmp_board=[[[]for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            for item in board[r][c]:
                m,d,s=item[0],item[1],item[2]
                nx = (r + dx[d] * s) % n
                ny = (c + dy[d] * s) % n
                tmp_board[nx][ny].append([m,d,s])
    board=copy.deepcopy(tmp_board)


def spread():
    for i in range(n):
        for j in range(n):
            m,s,even,odd=0,0,0,0
            if len(board[i][j])>=2:
                for item in board[i][j]:
                    m+=item[0]
                    s+=item[2]
                    if item[1]%2==0:
                        even+=1
                    else:
                        odd+=1
                m=m//5
                if m==0:
                    board[i][j]=[]
                    continue
                s=s//len(board[i][j])
                if odd==len(board[i][j]) or even==len(board[i][j]):
                    board[i][j]=[]
                    for dir in range(4):
                        board[i][j].append([m,dir*2,s])
                else:
                    board[i][j]=[]
                    for dir in range(4):
                        board[i][j].append([m,dir*2+1,s])

for _ in range(M):
    r,c,m,s,d=map(int,input().split())
    nx = (r-1 + dx[d] * s) % n
    ny = (c-1 + dy[d] * s) % n
    board[nx][ny].append([m, d, s])

spread()


for _ in range(k-1):
    move()
    spread()


total=0
for i in range(n):
    for j in range(n):
        for item in board[i][j]:
            total+=item[0]
print(total)
