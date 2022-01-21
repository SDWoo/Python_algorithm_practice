class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
            
        return answer



# [73,74,75,71,69,72,76,73] 이면, stack = [0] (1, 74 경우 73보다 크니까 answer = [1]
# 75도 같은 상황, stack = [2, 3, 4] 5, 72 경우에서 while문을 들어가니 answer[4] = 1, answer[3] = 2, stack = [2]
# 6, 76에서 75보다 크니가 anwer[2] = 4  so, [1,1,4,2,1, ...]