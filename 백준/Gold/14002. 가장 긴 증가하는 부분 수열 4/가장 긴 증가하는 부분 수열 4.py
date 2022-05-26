n=int(input())
arr=list(map(int,input().split()))
d=[1 for _ in range(n)]
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

    

