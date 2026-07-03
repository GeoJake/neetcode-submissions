class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = op = 0
        min_op = float("inf")
        for r in range(len(blocks)):
            if blocks[r] == "W":
                op += 1
            
            if r-l+1 >= k:
                min_op = min(min_op, op)
                if blocks[l] == "W":
                    op -= 1
                l += 1
        return min_op