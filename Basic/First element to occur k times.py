class Solution:
    def firstElementKTime(self,  a, n, k):
        ht={}
        for i in a:
            if i in ht:
                ht[i] +=1
                if ht[i]==k:
                    return i
            else:
                ht[i]=1
                if ht[i]==k:
                    return i
        
        return -1
