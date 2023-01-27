from collections import deque

def solution(prices):
    prices_que = deque(prices)
    answer = []
    
    while len(prices_que) > 0 :
        top = prices_que.popleft()
        time = 0
        for i in prices_que:
            if i >= top :
                time += 1
            else :
                time += 1
                break
        
        answer.append(time)
        
    return answer