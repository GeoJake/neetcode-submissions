class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        edges = {}
        ends = [0]
        res = 0

        for w in words:
            node = 0
            for i, ch in enumerate(w):
                key = node * 676 + (ord(ch) - 97) * 26 + ord(w[-1 - i]) - 97
                if key not in edges:
                    edges[key] = len(ends)
                    ends.append(0)
                node = edges[key]
                res += ends[node]
            ends[node] += 1
        return res