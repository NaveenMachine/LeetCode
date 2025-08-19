class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonic Decreasing Stack Solution
        # Ex: [73, 72, 71]
        
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([temp, i])
        return res
