class Solution:
    def maxTripletSum (self, arr,  n) : 
        if n ==3:
            return sum(arr)
        first=arr[0]
        second=float('-inf')
        third=float('-inf')
        for i in range(1,n):
            if arr[i]>first:
                third=second
                second=first
                first=arr[i]
                continue
            elif arr[i] >second:
                third=second
                second=arr[i]
                continue
            elif arr[i]>third:
                third=arr[i]
        return(first+second+third)
