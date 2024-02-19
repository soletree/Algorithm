def hanoi(from_, via, to, n, answer):
    if n == 1:
        answer.append([from_, to])
        return 
    hanoi(from_, to, via, n-1, answer)
    answer.append([from_, to])
    hanoi(via, from_, to, n-1, answer)
    
def solution(n):
    answer = []
    hanoi(1, 2, 3, n, answer)
    return answer