class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0

        for p in details:
            age = int(p[11:13])
            if age > 60:
                res += 1
                
        return res