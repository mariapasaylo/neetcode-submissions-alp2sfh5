class MedianFinder:

    def __init__(self):
        #create a max heap for smaller half and min heap for larger half
        self.maxH, self.minH = [],[]
        

    def addNum(self, num: int) -> None:
        #note that heapq in python is only min-heap
        #if min heap not empty and num > min in min heap
            #insert num to min heap
        #else
            #insert num into max heap

        if self.minH and num > self.minH[0]:
            heapq.heappush(self.minH, num)
        else:
            heapq.heappush(self.maxH,-1 * num)

        #rebalance the heaps if not the same size
        #if  size max heap > size min heap + 1
            #pop from max and push to min
        #if  size min heap > size max heap + 1
            #pop from min heap and push to max
        
        if len(self.maxH) > len(self.minH) + 1:
            val = -1 * heapq.heappop(self.maxH)
            heapq.heappush(self.minH, val)
        if len(self.minH) > len(self.maxH) + 1:
            val = -1 * heapq.heappop(self.minH)
            heapq.heappush(self.maxH, val)

    def findMedian(self) -> float:
        #if heaps same size
            #return top from min heap + top from max heap / 2.0
        #if size min heap > size max heap
            #return top of min heap
        #else
            #return top of max heap
        if len(self.maxH) == len(self.minH):
            return (self.minH[0] + (-1 * self.maxH[0])) / 2.0
        if len(self.minH) > len(self.maxH):
            return self.minH[0]
        return -1 * self.maxH[0]
        