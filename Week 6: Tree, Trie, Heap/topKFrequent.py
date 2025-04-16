import heapq
from typing import List
from collections import Counter

class Solution: 
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        # Goal is to determine the k most frequent elements
        # Time complexity must be better than O(n log n)

        # We have no choice but to iterate through the entire list once in order to perform the frequency count
        # O(n)
        freq_dict = Counter(nums)
        
        # After counting, we can sort the values by constructing a maxheap
        maxheap = [(-count, num) for num, count in freq_dict.items()]
        heapq.heapify(maxheap)
        
        result = []
        
        for _ in range(k):
            if maxheap:
                result.append(heapq.heappop(maxheap)[1])
                
        return result
    
    
    
print(Solution.topKFrequent([1,1,1,2,2,3], 2))
print(Solution.topKFrequent([1], 1))
print(Solution.topKFrequent([4,1,-1,2,-1,2,3], 2))

