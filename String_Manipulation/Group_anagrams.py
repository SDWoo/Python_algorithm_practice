# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = collections.defaultdict(list)

        for word in strs:
            ana[''.join(sorted(word))].append(word)

        return list(sorted(ana.values(), key=len))
