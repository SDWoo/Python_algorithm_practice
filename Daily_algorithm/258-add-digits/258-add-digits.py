class Solution:
    def addDigits(self, num: int) -> int:
        
        if num == 0:
            return 0
        lst: List = []
        while num:
            lst = list(map(int,str(num)))
            print(lst)
            if len(lst) == 1:
                return lst[0]
            else:
                num = sum(lst)