#User function Template for python3

class Solution:
    def minSubset(self, A,N):
        A.sort()
        pre=[]
        pre.append(A[0])
        for i in range(1,N):
            pre.append(pre[i-1]+A[i])
        
        j=N-2
        for i in range(N-2,-1,-1):
            if (pre[N-1]-pre[i])>pre[i]:
                return (N-1-i) 
        return N
