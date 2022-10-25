def solution(brown, yellow):
    brown=(brown-4)//2
    for row in range(1,brown):
        col=brown-row
        if col*row==yellow and col<=row:
            return [row+2,col+2]
    