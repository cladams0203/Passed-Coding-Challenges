
# arr = array of integers r = the common ratio
# example r = 2  arr = [ 1, 2, 2, 4]  output should be 2
from collections import defaultdict
def countTriplets(arr, r):
    pos2 = defaultdict(int)
    pos3 = defaultdict(int)
    count = 0;
    for i in arr:
        count += pos3[i]
        pos3[i * r] += pos2[i]
        pos2[i * r] += 1
    return count




print(countTriplets([1,5,5,25,125], 5))