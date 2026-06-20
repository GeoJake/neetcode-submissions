from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        timeStack = []

        for i in range(len(position)):
            cars.append([position[i], speed[i]])

        cars.sort(reverse=True, key=lambda x : x[0])

        for c in cars:
            time = (target - c[0])/c[1]
            if not timeStack or timeStack[-1] < time:
                timeStack.append(time)
        return len(timeStack)