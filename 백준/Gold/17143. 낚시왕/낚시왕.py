'''
r은 행, c는 열.
칸에는 상어가 최대 한 마리 들어있을 수 있다.
상어 크기, 속도
낚시왕은 가장 오른쪽 열의 오른쪽 칸에 이동하면 이동을 멈춤
1. 낚시왕이 오른쪽으로 한 칸 이동
2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다.
상어를 잡으면 격자판에서 잡은 상어가 사라진다.
3. 상어가 이동

상어는 입력으로 주어진 속도로 이동. 속도의 단위는 칸/초
상어가 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 방향을
반대로 바꿔서 속력을 유지한채로 이동.
상어가 보고 있는 방향이 속도의 방향, 왼쪽 아래에 적힌 정수는 속력
상어가 이동을 마친 후에 한 칸에 상어가 두마리 이상 있을 수 있다.
이때는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.
낚시왕이 상어 낚시를 하는 격자판의 상태가 주어졌을 때, 낚시왕이 잡은
상어 크기의 합을 구해보자.
'''
r,c,m=map(int,input().split())


board=[[[] for _ in range(c)] for _ in range(r)]

for i in range(m):
    #r,c는 상어의 위치, s는 속력, d는 이동방향, z는 크기
    #d가 1-위, 2-아래, 3-오른쪽, 4-왼쪽
    #두 상어가 같은 크기를 갖는 경우는 없고, 하나의 칸에 둘 이상의 상어가 있는 경우는 없다.
    p,q,s,d,z=map(int,input().split())
    board[p-1][q-1]=[s,d-1,z]

size_sum=0
dx=[-1,1,0,0]
dy=[0,0,1,-1]

def move_shark():
    tmp=[[[] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if len(board[i][j])!=0:
                speed,direct,size=board[i][j]
                x,y=i,j
                for num in range(speed):
                    nx=x+dx[direct]
                    ny=y+dy[direct]
                    if nx<0 or nx>=r or ny<0 or ny>=c:
                        if direct==0 or direct==2:
                            direct+=1
                        else:
                            direct-=1
                        nx=x+dx[direct]
                        ny=y+dy[direct]
                    x,y=nx,ny
                if tmp[x][y]!=[]:
                    if tmp[x][y][2]<size:
                        tmp[x][y]=[]
                        tmp[x][y]=[speed,direct,size]
                else:
                    tmp[x][y]=[speed,direct,size]
    for i in range(r):
        for j in range(c):
            board[i][j]=tmp[i][j]



for i in range(c):
    for j in range(r):
        if board[j][i]!=[]:
            size_sum+=board[j][i][2]
            board[j][i] = []
            break
    move_shark()
print(size_sum)