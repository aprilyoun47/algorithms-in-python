"""
주식 가격(QUE)
https://school.programmers.co.kr/learn/courses/30/lessons/42584
- 이중 for문으로 -> que를 사용해보자
- 몇 분 동안 주식 가격이 하락하지 않는지 for문
해당 금액에서 전체 list를 돌면서 가격 비교를 해야함. 해당 금액부터 start 이므로 
"""

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
