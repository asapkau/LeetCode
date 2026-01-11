class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for w in strs:
            key = "".join(sorted(w))

            if key not in hashMap:
                hashMap[key] = []
            hashMap[key].append(w)

        return list(hashMap.values())
        