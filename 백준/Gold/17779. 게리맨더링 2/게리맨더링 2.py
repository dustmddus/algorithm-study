
n=int(input())

board=[[0 for _ in range(n+1)]]

total=0
#사람 수
for i in range(n):
    data=[0]+list(map(int,input().split()))
    board.append(data)
    total+=sum(data)

min_diff=1e9
def search(x,y,d1,d2):
    global min_diff
    #구역 저장
    g=[[0]*(n+1) for _ in range(n+1)]
    #사람
    people=[0,0,0,0,0]
    #경계선
    g[x][y]=5
    for i in range(1,d1+1):
        g[x+i][y-i]=5
    for i in range(1,d2+1):
        g[x+i][y+i]=5
    for i in range(1,d2+1):
        g[x+d1+i][y-d1+i]=5
    for i in range(1,d1+1):
        g[x+d2+i][y+d2-i]=5

    #각 구역 사람 구하기

    #1
    for i in range(1,x+d1):
        for j in range(1,y+1):
            if g[i][j]==5:
                break
            else:
                people[0]+=board[i][j]
    #2
    for i in range(1,x+d2+1):
        for j in range(n,y,-1):
            if g[i][j]==5:
                break
            else:
                people[1]+=board[i][j]
    #3
    for i in range(x+d1,n+1):
        for j in range(1,y-d1+d2):
            if g[i][j]==5:
                break
            else:
                people[2]+=board[i][j]
    #4
    for i in range(x+d2+1,n+1):
        for j in range(n,y-d1+d2-1,-1):
            if g[i][j]==5:
                break
            else:
                people[3]+=board[i][j]
    people[4]=total-sum(people[0:4])
    min_diff=min(min_diff,max(people)-min(people))


for x in range(1,n+1):
    for y in range(1,n+1):
        for d1 in range(1,n+1):
            for d2 in range(1,n+1):
                if x+d1+d2>n:
                    continue
                if y-d1<1:
                    continue
                if y+d2>n:
                    continue
                search(x,y,d1,d2)

print(min_diff)