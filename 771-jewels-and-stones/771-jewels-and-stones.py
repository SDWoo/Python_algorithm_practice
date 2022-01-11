class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = collections.Counter(stones)
        count = 0
        
        for char in jewels:
            count += freq[char]
            
        return count