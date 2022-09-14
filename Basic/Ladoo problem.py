#User function Template for python3

class Solution:
    def divideLadoo(self, N, A):
        ht={}
        for i in A:
            if i in ht:
                ht[i] +=1
            else:
                ht[i]=1
        
        count=0
        for key in ht.keys():
            count +=1
        return count
