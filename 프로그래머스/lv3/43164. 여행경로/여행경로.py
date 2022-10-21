'''
주어진 항공권을 모두 이용해 여행 경로 짜려 한다.
icn에서 출발
[a,b] a공항에서 b공항으로 가는 항공권이 있다는 의미
'''
import copy

def solution(tic):
    start = []
    for item in tic:
        if item[0] == 'ICN':
            start.append(item)
    visited = copy.deepcopy(tic)
    result = []
    tic.sort()
    def dfs(arr, n):
        if n == len(tic):
            visited.sort()
            if len(visited)==0:
                result.append(arr)
            return
        for i in tic:
            if i in visited and arr[-1] == i[0]:
                visited.remove(i)
                tmp_arr=copy.deepcopy(arr)
                tmp_arr.append(i[1])
                dfs(tmp_arr, n + 1)
                visited.append(i)

    for item in start:
        visited.remove(item)
        dfs(item, 1)
        visited.append(item)
    result.sort()
    return result[0]