class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        Map = {}

        for i in nums:
            Map[i] = Map.get(i, 0) + 1

        top_k = sorted(Map, key=Map.get, reverse=True)[:k]
        return top_k

        