from collections import deque
#1~n 반지름 원판, m개의 정수, T번 회전
n,m,t=map(int,input().split())

#원판에 적힌 수
board=[deque(list(map(int,input().split()))) for _ in range(n)]
roll=[list(map(int,input().split())) for _ in range(t)]

#1. 회전 시켜라
for tc in range(t):
    result=0
    x,d,k=roll[tc]
    for i in range(n):
        result+=sum(board[i])
        if (i+1)%x==0:
            if d==0:
                board[i].rotate(k)
            else:
                board[i].rotate(-k)


    if result!=0:
        remove_item = []
        #한 원판에서 인접한 것 찾기
        for i in range(n):
            for j in range(m-1):
                if board[i][j]!=0 and board[i][j+1]!=0 and board[i][j]==board[i][j+1]:
                    remove_item.append((i,j))
                    remove_item.append((i,j+1))
            if board[i][m-1]!=0 and board[i][0]!=0 and board[i][0]==board[i][m-1]:
                remove_item.append((i,m-1))
                remove_item.append((i,0))
        #위 아래 원판 인접한 것 찾기
        for j in range(m):
            for i in range(n-1):
                if board[i][j]!=0 and board[i+1][j]!=0 and board[i][j]==board[i+1][j]:
                    remove_item.append((i,j))
                    remove_item.append((i+1,j))

        remove_item=list(set(remove_item))

        for x,y in remove_item:
            board[x][y]=0

        if len(remove_item)==0:
            avg_sum=0
            zero=0
            for i in range(n):
                avg_sum+=sum(board[i])
                zero+=board[i].count((0))
            avg=avg_sum/(m*n-zero)

            for i in range(n):
                for j in range(m):
                    if board[i][j]!=0 and board[i][j]>avg:
                        board[i][j]-=1
                    elif board[i][j]!=0 and board[i][j]<avg:
                        board[i][j]+=1

    else:
        break

total=0
for i in range(n):
    total+=sum(board[i])

print(total)