class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHashMap = {}
        tHashMap = {}

        if len(s) != len(t):
            return False
        for i in s:
            sHashMap[i] = sHashMap.get(i,0) + 1
        for i in t:
            tHashMap[i] = tHashMap.get(i,0) + 1

        if sHashMap == tHashMap:
            return True
        return False
