class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        good = set()

        for i in range(len(triplets)):
            trip = triplets[i]
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue

            for j in range(len(trip)):                
                if trip[j] == target[j]:
                    good.add(j)
        
        return len(good) == len(target)