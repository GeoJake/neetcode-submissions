from collections import deque
class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {} # (l_char, r_char) : TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c1, c2 in zip(word, reversed(word)):
            if (c1, c2) not in curr.children:
                curr.children[(c1, c2)] = TrieNode()
            curr = curr.children[(c1, c2)]
            curr.count += 1

    def count(self, word):
        curr = self.root
        for c1, c2 in zip(word, reversed(word)):
            if (c1, c2) not in curr.children:
                return 0
            curr = curr.children[(c1, c2)]
        return curr.count

    def print(self):
        d = deque([(self.root, 0)])
        while d:
            curr, tabs = d.pop()
            for c in curr.children.keys():
                for _ in range(tabs):
                    print("\t", end="")
                print(f"{c} Count: {curr.children[c].count}")
                d.append((curr.children[c], tabs + 1))

class Solution:

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        root = Trie()
        res = 0
        for w in reversed(words):
            res += root.count(w)
            # root.print()
            root.insert(w)
        return res