def solution(n):
    r=[]
    sum=0
    while n//3!=0:
        r.append(n%3)
        n=n//3
    r.append(n)
    k=len(r)-1
    for i in r:
        sum+=i*3**k
        k-=1
    return sum