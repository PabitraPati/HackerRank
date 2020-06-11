"""
Given an array of integers ar, return the maximum difference of any pair of number such 
that the larger integer is  the pair occurs at a higher index ( in the array) than the 
smaller integer. Return -1 if you can't find any such pair.

[8,3,10,2,4,8,1]  ---> 
answer would be 7, because 10 is larger and it's position in array is 2. 
Even though 1 is smallest in arrya, but index of 1 is 6 which is higher than index of 10. 
so integer with lower index than 10 is 3. so the difference is 10-3 =7

"""

def maxDifference(ar):
    prev = ar[0]
    maxVal = ar[0]
    minVal = ar[0]
    diff = []
    
    for item in ar[1:]:
        if prev > item:
            diff.append(maxVal -minVal)
            print(diff)
            maxVal = item
        minVal = item if item < minVal else minVal
        maxVal = item if item > maxVal else maxVal
        prev = item
    diff.append(maxVal -minVal)
 
    ret = max(diff)
    if ret == 0 :
        ret = -1
    print(ret)
    return ret

a = [2,3,10,2,4,8,1]
b = [7,9,5,6,3,2]
c = [7,10,4,3,8,2,1,6]

maxDifference(a)
maxDifference(b)
maxDifference(c)
