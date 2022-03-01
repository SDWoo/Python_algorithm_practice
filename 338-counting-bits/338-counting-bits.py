class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        while n > 0:
            num = str(bin(n)).count("1")
            result.append(num)
            n -= 1
            
        result.append('0') 
        return reversed(result)