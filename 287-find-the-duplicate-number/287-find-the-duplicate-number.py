class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        occurence={}
        for i in nums:
            if i in occurence:
                occurence[i]+=1
            else:
                occurence[i]=1
        for dublicateVal in occurence:
            if occurence[dublicateVal]>1:
                return dublicateVal