class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        out = set()
        candidates.sort()

        def helper(total, subset, idx):
            if target == total:
                out.add(tuple(subset.copy()))
                return
            if target < total or idx >= len(candidates):
                return
            
            subset.append(candidates[idx])
            helper(total + candidates[idx], subset, idx+1)

            subset.pop()
            helper(total, subset, idx+1)

        helper(0, [], 0)

        return [list(subset) for subset in out] 
        """

        out = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                out.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return
            
            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i])

            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            dfs(i+1, cur, total)

        dfs(0, [], 0)

        return out