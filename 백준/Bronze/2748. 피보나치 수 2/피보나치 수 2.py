'''
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램.
d[i]=d[i-1]+d[i-2]
d[0]=0
d[1]=1


'''
n=int(input())
d=[0]*(n+1)
d[1]=1
for i in range(2,n+1):
    d[i]=d[i-1]+d[i-2]
print(d[n])
