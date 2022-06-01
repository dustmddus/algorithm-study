n,m=map(int,input().split())
li=list(map(int,input().split()))
li.sort()
arr=[0 for _ in range(10)]


def func(k):
    if k==m:
        for i in range(m):
            print(li[arr[i]],end=' ')
        print()
        return
    st=0
    if k!=0:st=arr[k-1]
    for i in range(st,n):
            arr[k]=i
            func(k+1)
func(0)
