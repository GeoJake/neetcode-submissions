class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    # [1, 2, 3, 4], target = 3
    # [1 , 2]
    # 1-indexed

        n = len(numbers)

        low = 0
        high = n-1
        
        while(low < high):
            
            total = numbers[high] + numbers[low]

            if total > target:
                high -= 1

            elif total < target:
                low += 1

            elif total == target:
                return [low+1, high+1]
        
        return []