class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiantSet = set()
        direSet = set()
        bannedSet = set()

        radiantToBan = 0
        direToBan = 0


        for i, c in enumerate(senate):
            if c == "R":
                radiantSet.add(i)
            elif c == "D":
                direSet.add(i)

        while radiantSet and direSet:
            for i, c in enumerate(senate):
                if i in bannedSet:
                    continue
                elif c == "R":
                    if radiantToBan:
                        radiantSet.discard(i)
                        bannedSet.add(i)
                        radiantToBan -= 1
                    else:
                        direToBan += 1
                elif c == "D":
                    if direToBan:
                        direSet.discard(i)
                        bannedSet.add(i)
                        direToBan -= 1
                    else:
                        radiantToBan += 1
        
        if radiantSet:
            return "Radiant"
        else:
            return "Dire"
