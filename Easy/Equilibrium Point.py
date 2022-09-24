class Solution:
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        if N ==1:
            return 1
        prefix=[0]*N
        prefix[0]=A[0]
        for i in range(1,N):
            prefix[i] = A[i]+prefix[i-1]
        
        for i in range(1,N):
            if prefix[i-1] == (prefix[N-1]-prefix[i]):
                return i+1
        return -1
