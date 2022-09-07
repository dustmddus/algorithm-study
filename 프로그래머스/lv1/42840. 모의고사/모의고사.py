'''
1번-1,2,3,4,5
2번-2,1,2,3,2,4,2,5
3번-3,3,1,1,2,2,4,4,5,5
가장 많은 문제를 맞힌 사람이 누구인가. 
'''
def solution(answers):
    result=[0,0,0]
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i]==one[i%5]:
            result[0]+=1
        if answers[i]==two[i%8]:
            result[1]+=1
        if answers[i]==three[i%10]:
            result[2]+=1
    answer=[]
    for i in range(len(result)):
        if max(result)==result[i]:
            answer.append(i+1)
    return answer
    