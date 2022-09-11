def solution(array, commands):
    ans=[]
    for i,j,k in commands:
        temp=sorted(array[i-1:j])
        ans.append(temp[k-1])
    return(ans)