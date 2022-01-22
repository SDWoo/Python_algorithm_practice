import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)

# Solution2

class Solution2:
    def numJewelsInstones1(self, jewels: str, stones: str) -> int:
        freqs = {}

        for char in stones:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] +=1

        count = 0

        for char in jewels:
            if char in freqs:
                count += freqs[char]

        return count

# Soltion 3
class Solution3:
    def numJewelsinStones2(self, j: str, s: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        for char in s:
            freqs[char] += 1

        for char in j :
            count += freqs[char]

        return count

# Solution4
class Solution4:
    def jins(self, j:str, s:str) -> int:
        freqs = collections.Counter(s)
        count = 0
        for char in j:
            count += freqs[char]

        return count

