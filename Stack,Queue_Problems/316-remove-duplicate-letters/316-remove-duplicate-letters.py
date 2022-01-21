class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []
        
        for char in s:
            counter[char] -=1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
                
            stack.append(char)
            seen.add(char)
            
        return ''.join(stack)

# Solution2
class Solution2:
    def removeDuplicateLetters2(self, s: str) -> str:
        print(s)
        print(set(s))
        print(sorted(set(s)))
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters2(suffix.replace(char, ''))
        return ''



