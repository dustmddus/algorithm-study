def solution(n):
    s=format(n,'b')
    one=s.count('1')
    
    for i in range(n+1,1000001):
        tmp=format(i,'b')
        if tmp.count('1')==one:
            return i