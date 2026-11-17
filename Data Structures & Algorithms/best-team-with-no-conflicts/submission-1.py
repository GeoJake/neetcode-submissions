class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """
        1 2 5 3 3 3 3 3
        2 2 2 5 5 5 5 5

        1 + 2 + 5 = 8
        1 + 2 + _ + (3 * 5) = 18

        1 2 3 3 3 3 3 5
        2 6 5 5 5 5 5 2
        """

        pairs = [[scores[i], ages[i]] for i in range(len(scores))]
        pairs.sort() 

        dp = [pairs[i][0] for i in range(len(pairs))]

        for i in range(len(pairs)):
            mScore, mAge = pairs[i]
            for j in range(i):
                score, age = pairs[j]
                if mAge >= age:
                    dp[i] = max(dp[i], mScore + dp[j])
        
        return max(dp)