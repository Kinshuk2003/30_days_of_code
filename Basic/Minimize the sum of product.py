class Solution:
    def minValue(self, a, b, n):
        a.sort()
        b.sort(reverse=True)
        ans=0
        for i in range(0,n):
            ans +=(a[i]*b[i])
        
        return ans
