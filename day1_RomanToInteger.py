#leet code problem 13
#Roman Number to Decimal converter
def romanToInt( s: str) -> int:
    Roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    num = Roman[s[len(s)-1]]
    sum = 0
    for i in range(0,len(s)-1):
        if Roman[s[i+1]] <= Roman[s[i]]:
            sum = sum+Roman[s[i]]
        else :
            sum = sum-Roman[s[i]]
    sum = sum + num
    return sum

#Driver code
s = input()
x = romanToInt(s)
print(x)
