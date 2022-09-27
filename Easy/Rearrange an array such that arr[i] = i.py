class Solution:
    def modifyArray (self, arr,  n) : 
        ht={}
        for i in arr:
            if i in ht:
                ht[i] +=1
            else:
                ht[i]=1
        
        ans=[-1]*n
        for i in range(0,n):
            if i in ht:
                ans[i]=i
        
        return ans
