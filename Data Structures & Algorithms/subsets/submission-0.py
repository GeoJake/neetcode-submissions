class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(n, subset):
            if not n:
                res.append(subset.copy())
                return

            val = n[0]
            helper(n[1:], subset)
            subset.append(val)
            helper(n[1:], subset)
            subset.pop()
            
        helper(nums, [])

        return res