import sys
sys.setrecursionlimit(10**9)

n=int(input())
adj=[[] for _ in range(n+1)]
p=[0]*(n+1)
for i in range(n-1):
    x,y=map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)
def dfs(cur):
    for i in adj[cur]:
        if p[cur]==i:
            continue
        p[i]=cur
        dfs(i)
dfs(1)
for i in range(2,n+1):
    print(p[i])
