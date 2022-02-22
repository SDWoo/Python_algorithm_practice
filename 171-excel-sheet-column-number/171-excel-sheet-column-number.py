class Solution:
    from string import ascii_uppercase
    def titleToNumber(self, columnTitle: str) -> int:
        if not columnTitle:
            return 0
        
        alphabet_dict = {}
        stack = []
        result = 0
        
        for i, n in enumerate(ascii_uppercase):
            alphabet_dict[n] = i+1
            
        if len(columnTitle) == 1:
            return alphabet_dict[columnTitle]
                                 
                                 
        for s in columnTitle:
            stack.append(s)
            print(stack)
        
        index = 0
        while stack:
            result += alphabet_dict[stack.pop()] * 26 ** index
            print(result)
            index += 1
            
        return result
        
        
        