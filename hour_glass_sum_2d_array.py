
def hourglassSum(arr):
    # number of sub arrays traversed
    sub_array_count = 0
    max_sum = None
    for i in arr:
        if sub_array_count < 4:
            for idx, num in enumerate(i):
                total_hourglass = -1000
                if idx + 2 < 6:
                    level1 = arr[sub_array_count][idx] + arr[sub_array_count][idx + 1] + arr[sub_array_count][idx + 2]
                    level2 = arr[sub_array_count + 1][idx + 1]
                    level3 = arr[sub_array_count + 2][idx] + arr[sub_array_count + 2][idx + 1] + arr[sub_array_count + 2][idx +2]
                    total_hourglass = level1 + level2 + level3
                if max_sum == None:
                    max_sum = total_hourglass
                if total_hourglass > max_sum:
                    max_sum = total_hourglass

        sub_array_count += 1
    return max_sum

print(hourglassSum([[-1,-1,0,-9,-2,-2], [-2,-1,-6,-8,-2,-5],[-1,-1,-1,-2,-3,-4],[-1,-9,-2,-4,-4,-5],[-7,-3,-3,-2,-9,-9],[-1,-3,-1,-2,-4,-5]]))

#example 2d array for hourglass
# -9 -9 -9  1  1  1
#  0 -9  0  4  3  2
# -9 -9 -9  1  2  3
#  0  0  8  6  6  0
#  0  0  0 -2  0  0
#  0  0  1  2  4  0

#hourglass example
#  -9 -9 -9
#     -9
#  -9 -9 -9

#only 16 hourglasses in 2d array

# results should be
#  -63 -34  -9  12
#  -10   0  28  23
#  -27 -11  -2  10
#    9  17  25  18

# return highest value