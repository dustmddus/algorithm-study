'''
수열 A가 주어졌을 떄, 가장 긴 증가하는 부분수
1. 테이블 정하기
d[i]=i까지 증가하는 가장 큰 수
2.. 점화식
'''
n=int(input())
d=[1 for _ in range(n)]
arr=list(map(int,input().split()))

for i in range(n):
    for j in range(i):
        if arr[i]>arr[j]:
            d[i]=max(d[i],d[j]+1)
print(max(d))
order=max(d)
result=[]
for i in range(n-1,-1,-1):
    if d[i]==order:
        result.append(arr[i])
        order-=1
result.reverse()
print(*result)
