from collections import deque

def bfs(n):
    vis=[0]*100001
    q=deque()
    q.append(n)
    while q:
        cur=q.popleft()
        if cur==k:
            return vis[cur]
        for next_num in (cur-1,cur+1,cur*2):
            if 0<=next_num<100001:
                if vis[next_num]==0:
                    if next_num==2*cur and cur!=0:
                        vis[next_num]=vis[cur]
                        q.appendleft(next_num)
                    else:
                        vis[next_num]=vis[cur]+1
                        q.append(next_num)
n,k=map(int,input().split())
print(bfs(n))
                
