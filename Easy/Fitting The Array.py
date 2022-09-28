class Solution:
    def isFit (self,arr, brr, n) : 
        
        arr.sort()
        brr.sort()
        
        f=0
        for i in range(n):
            if arr[i] <= brr[i]:
                continue
            else:
                f=1
                break
        
        if f==1:
            return False
        else:
            return True
