t,w=map(int,input().split())
arr=[1]
d=[[0]*(w+1) for _ in range(t+1)]
for i in range(t):
    x=int(input())
    arr.append(x)
for i in range(1,t+1):
    if arr[i]==1:
        for j in range(w+1):
            if j%2==0:
                if j==0:
                    d[i][j]=d[i-1][0]+1
                else:
                    d[i][j]=max(d[i-1][j-1],d[i-1][j])+1
            else:
                d[i][j]=d[i-1][j]
    else:
        for j in range(w+1):
            if j%2==0:
                d[i][j]=d[i-1][j]
            else:
                d[i][j]=max(d[i-1][j-1],d[i-1][j])+1
print(max(d[t]))
    
