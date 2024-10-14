class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #Key: number of times
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n,c in count.items():
            freq[c].append(n)
        
        ans = []
        for i in range(len(freq) - 1,-1 , -1):
            for num in freq[i]:
                if len(ans) == k:
                    return ans
                ans.append(num)
        
        return ans