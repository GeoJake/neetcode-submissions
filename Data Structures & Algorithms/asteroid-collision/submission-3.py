from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        

        """
        -5, 3, 4, -1, -5, 4

        :(-5, 0), (-1, 3), (-5, 4)
        :
        """

        pos = deque([])
        neg = deque([])

        for i, a in enumerate(asteroids):
            
            if a > 0:
                pos.append((a, i))
            else:
                neg.append((a, i))

            while pos and neg and pos[-1][1] < neg[-1][1]:

                pA = abs(pos[-1][0])
                nA = abs(neg[-1][0])

                if pA > nA:
                    neg.pop()
                elif pA < nA:
                    pos.pop()
                else:
                    neg.pop()
                    pos.pop()

        res = []

        while pos or neg:
            if pos and neg and pos[0][1] < neg[0][1]:
                res.append(pos[0][0])
                pos.popleft()
            elif pos and neg and pos[0][1] > neg[0][1]:
                res.append(neg[0][0])
                neg.popleft()
            elif pos:
                res.append(pos[0][0])
                pos.popleft()
            elif neg:
                res.append(neg[0][0])
                neg.popleft()

        return res