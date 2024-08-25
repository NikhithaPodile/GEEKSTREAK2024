#User function Template for python3
import heapq

class Solution:

    def kthSmallest(self, arr, k):
        heapq.heapify(arr)
        for _ in range(k - 1):
            heapq.heappop(arr)
        return heapq.heappop(arr)