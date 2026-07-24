class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded_str = ""
        
        for s in strs:
            l = len(s)
            encoded_str += f"{l}/{s}"
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs = []
        start_size_idx = -1
        i = 0

        while i < len(s):
            if start_size_idx < 0 and s[i] >= "0" and s[i] <= "9":
                start_size_idx = i
            elif s[i] == "/":
                str_len = int(s[start_size_idx:i])
                strs.append(s[i+1:i + str_len + 1])
                start_size_idx = -1
                i += str_len
            i += 1
        return strs