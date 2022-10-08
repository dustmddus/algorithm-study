#한 변의 길이 n, 나무의 개수 m, k년
n,m,k=map(int,input().split())

#배열 a -> 각 칸의 양분의 양
plus=[list(map(int,input().split())) for _ in range(n)]

#양분 배열
soil=[[5]*n for _ in range(n)]

#한 칸에 속한 나무 나이 모음

trees=[[[] for _ in range(n)] for _ in range(n)]

#이동 방향
dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]

#상도가 심은 나무의 정보 m 개
for i in range(m):
    x,y,z=map(int,input().split())
    trees[x-1][y-1].append(z)

for year in range(k):
    #봄,여름
    for i in range(n):
        for j in range(n):
            dead=0
            tmp=[]
            if trees[i][j]:
                trees[i][j].sort()
                for age in trees[i][j]:
                    if soil[i][j]<age:
                        dead+=age//2
                    else:
                        soil[i][j]-=age
                        tmp.append(age+1)
                soil[i][j]+=dead
                trees[i][j]=tmp
    for i in range(n):
        for j in range(n):
            soil[i][j]+=plus[i][j]
            for tree in trees[i][j]:
                if tree%5==0:
                    for dir in range(8):
                        nx=i+dx[dir]
                        ny=j+dy[dir]
                        if nx<0 or nx>=n or ny<0 or ny>=n:
                            continue
                        trees[nx][ny].append(1)

result=0
for i in range(n):
    for j in range(n):
        result+=len(trees[i][j])
print(result)


