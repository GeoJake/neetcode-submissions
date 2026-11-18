class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0

        if len(words) == 1:
            return res

        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):

                if (len(words[i]) <= len(words[j]) and 
                words[i] == words[j][:len(words[i])] and 
                words[i] == words[j][-len(words[i]):]):
                    res += 1
        
        return res