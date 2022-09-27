class Solution:
    def smallestSumSubarray(self, A, N):
        min_so_far= float('inf')
        min_till_now=float('inf')
        
        for i in range(0,N):
            if min_so_far > 0:
                min_so_far=A[i]
            else:
                min_so_far +=A[i]
            
            min_till_now=min(min_till_now,min_so_far)
            
        return min_till_now
