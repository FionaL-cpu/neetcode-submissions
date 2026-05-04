class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minheap with k largest numbers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) #o(n)
        while len(self.minHeap) > k: 
            heapq.heappop(self.minHeap)
   

    def add(self, val: int) -> int:
        # add val in heap
        heapq.heappush(self.minHeap, val)   #  m (log k)
        # pop smallest if the len > k
        if len(self.minHeap) >self.k:
            heapq.heappop(self.minHeap)       # m (log k)

        return self.minHeap[0]
