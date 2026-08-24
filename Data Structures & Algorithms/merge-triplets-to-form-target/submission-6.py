class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = False

        for trip in triplets:
            if trip[0] == target[0] and trip[1] <= target[1] and trip[2] <= target[2]:
                x = True
            if trip[0] <= target[0] and trip[1] == target[1] and trip[2] <= target[2]:
                y = True
            if trip[0] <= target[0] and trip[1] <= target[1] and trip[2] == target[2]:
                z = True
            if x and y and z:
                return True
        
        return False