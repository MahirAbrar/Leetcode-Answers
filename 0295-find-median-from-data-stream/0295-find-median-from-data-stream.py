class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []   #maxHeap, minHeap
        ## [1,2] [3,4,5,6]

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, num * - 1)
            
        #balancing 
        #small >= right
        if len(self.small) > len(self.large) + 1:   #more values in small
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)
            
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1)
            

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
           return (((self.small[0] * -1) + self.large[0]) / 2)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()