#User function Template for python3

def isSubset( a1, a2, n, m):
    if m > n:
        return "No"
    ht={}
    for i in a1:
        if i in ht:
            ht[i] +=1
        else:
            ht[i] =1
    
    for i in a2:
        if i in a1 and ht[i]>=1:
            ht[i] -=1
        else:
            return "No"
    return "Yes"
    
