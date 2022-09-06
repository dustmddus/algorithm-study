def solution(numbers):
    result=[]
    for i in numbers:
        bin_num=list('0'+format(i,'b'))
        idx=''.join(bin_num).rfind('0')
        bin_num[idx]='1'
        if i%2!=0:
            bin_num[idx+1]='0'
        result.append(int(''.join(bin_num),2))
    return result
            