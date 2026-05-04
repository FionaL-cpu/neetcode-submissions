class MedianFinder:

    def __init__(self):
        # small - maxHeap, large - minHeap
        self.small, self.large =[],[]
        # small[0] --maxvalue in the heap [-10, -9, -6, 0]
        # large[0] --min value in the heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]): # need to move
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.small) > len(self.large) + 1: #move to large
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1: #move to small
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)


        
        

    def findMedian(self) -> float:
        # median index 
        if not self.small and not self.large:
            return
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]
        else: 
            return  (-1 * self.small[0] + self.large[0]) / 2
       
        
        
        