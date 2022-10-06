import sys

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        curr_sum=0
        max_sum=-sys.maxsize-1
        for i in range(0,N):
            curr_sum += arr[i]
            if max_sum < curr_sum:
                max_sum=curr_sum
            
            if curr_sum <0:
                curr_sum=0

        return max_sum
