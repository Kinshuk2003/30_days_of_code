class Solution:
    def ReFormatString(self,S, K):
        st=""
        for i in S:
            if i=='-':
                continue
            elif i.islower():
                st +=i.upper()
            else:
                st +=i
        
        ans=""
        n=len(st)
        r=n%K
        if r!=0:
            ans +=st[:r]
            if r != n:
                ans +='-'
        for i in range(r,n,K):
            ans +=st[i:i+K]
            if (i+K)!=n:
                ans +='-'
    
        return ans
