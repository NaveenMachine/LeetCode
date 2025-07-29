class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        SortedFreq = {}

        for n in nums:
            if n in SortedFreq:
                SortedFreq[n] += 1
            else:
                SortedFreq[n] = 1

        sortedFreqs = []
        
        # sort Map by value in array
        SortedMap = sorted(SortedFreq.items(), key = lambda item: item[1], reverse=True)
        
        result = [key for key,value in SortedMap[:k]]

        return result
            
