'''
n개의 시험장. 
총 감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 b명. 
부감독관은 c명
각 시험장에 총감독관은 오직 1명, 부감독관은 여러명 괜춘
각 시험장마다 응시생들을 모두 감시해야 한다. 
필요한 감독관 수의 최솟값을 구하는 프로그램. 
'''
import math
n = int(input())

board = list(map(int, input().split()))

b, c = map(int, input().split())
result = 0
for i in board:
    result += 1
    if i-b>0:
      result += math.ceil((i-b) / c)

print(result)
