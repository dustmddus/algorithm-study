n,m=map(int,input().split())
li=list(map(int,input().split()))
arr=[0 for _ in range(10)]
isused=[0 for _ in range(10)]
li.sort()

def func(k):
    if k==m:
        for i in range(m):
            print(arr[i],end=' ')
        print()
        return
    tmp=0
    for i in range(n):
        if isused[i]==0 and tmp!=li[i]:
            isused[i]=1
            arr[k]=li[i]
            tmp=arr[k]
            func(k+1)
            isused[i]=0
        
func(0)
