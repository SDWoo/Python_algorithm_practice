# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents.
# If their contents are the same, then sort them lexicographically by their identifiers.
# The digit-logs maintain their relative ordering.

# Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
# Solution
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # sort with lambda
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
