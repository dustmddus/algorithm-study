'''
1. 테이블 잡기
d[i]=i일에 얻을 수 있는 최대 수익
2. 점화식
d[i]=만약 i+t[i]가 n보다 크다면 d[i]=d[i+1]
그렇지 않다면 d[i]=max(d[i+1],d[i+t[i]]+p[i])
'''
n=int(input())
t,p=[],[]
for i in range(n):
  a,b=map(int,input().split())
  t.append(a)
  p.append(b)

dp=[0]*(n+1)

for i in range(n-1,-1,-1):
  if i+t[i]>n:
    dp[i]=dp[i+1]
  else:
    dp[i]=max(dp[i+1],dp[i+t[i]]+p[i])

print(dp[0])

