class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}
        s2_freq = {}
        matches = 0

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            if s1[i] in s1_freq:
                s1_freq[s1[i]] += 1
            else:
                s1_freq[s1[i]] = 1

        for i in range(len(s1)):
            if s2[i] in s2_freq:
                s2_freq[s2[i]] += 1
            else:
                s2_freq[s2[i]] = 1
        
        for key, val in s1_freq.items():
            if key in s2_freq and val == s2_freq[key]:
                matches += 1

        l = 0

        for r in range(len(s1), len(s2)):
            
            if matches == len(s1_freq):
                return True

            if s2[r] in s2_freq:
                s2_freq[s2[r]] += 1
            else:
                s2_freq[s2[r]] = 1

            if s2[r] in s1_freq and s1_freq[s2[r]] == s2_freq[s2[r]]:
                matches += 1
            elif s2[r] in s1_freq and s1_freq[s2[r]] + 1 == s2_freq[s2[r]]:
                matches -= 1
            
            if s2[l] in s2_freq:
                s2_freq[s2[l]] -= 1
            else:
                s2_freq[s2[l]] = 0

            if s2[l] in s1_freq and s1_freq[s2[l]] == s2_freq[s2[l]]:
                matches += 1
            elif s2[l] in s1_freq and s1_freq[s2[l]] - 1 == s2_freq[s2[l]]:
                matches -= 1

            l += 1

    

        return matches == len(s1_freq)