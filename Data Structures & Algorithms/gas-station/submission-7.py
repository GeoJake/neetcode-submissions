class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        start = 0
        tank = 0

        for end in range(n):
            tank += gas[end] - cost[end]

            if tank < 0:
                start = end + 1
                tank = 0
        
        return start
            