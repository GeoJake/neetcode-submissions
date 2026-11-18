class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0

        if len(words) == 1:
            return res

        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                w1, w2 = words[i], words[j]
                if w2.startswith(w1) and w2.endswith(w1):
                    res += 1
        return res