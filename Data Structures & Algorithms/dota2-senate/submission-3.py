from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiantQ = deque([])
        direQ = deque([])

        for i, c in enumerate(senate):
            if c == "R":
                radiantQ.append(i)
            elif c == "D":
                direQ.append(i)

        n = len(senate)

        while radiantQ and direQ:
            rVal = radiantQ.popleft()
            dVal = direQ.popleft()

            if rVal < dVal:
                rVal += n
                radiantQ.append(rVal)
            else:
                dVal += n
                direQ.append(dVal)
            
        if radiantQ:
            return "Radiant"
        else:
            return "Dire"