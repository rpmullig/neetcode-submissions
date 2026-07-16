class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonic_stack: List[int] = list()
        result: List[int] = [0] * len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            current_temperature: int = temperatures[i]
            while len(monotonic_stack) > 0 and temperatures[monotonic_stack[-1]] <= current_temperature:
                monotonic_stack.pop()
            if len(monotonic_stack) > 0:
                result[i] = monotonic_stack[-1] - i
            else:
                result[i] = 0 
            monotonic_stack.append(i)

        return result