import time


f = open('input04.txt', 'r')
lines = list(f)
data = []
for i in lines:
    data.append(i.strip().split(' '))
data = [[int(y) for y in x]for x in data]
data.pop(0)

start_time = time.time()



def arrayManipulation(n, queries):

### ---- .007 seconds WOW!! -----###
###-- this is called difference and prefix --##
    array = [0] * (n + 1)
    for i in queries:
        array[i[0] - 1] += i[2]
        array[i[1]] -= i[2]
    max = 0
    sum = 0
    for i in array:
        sum += i
        if sum > max:
            max = sum
    end_time = time.time()
    print(end_time - start_time)
    return max

    # ---- 7.09 seconds-----#
    # array = [0] * n
    # length = len(queries)
    # position = 0
    # start = queries[position][0] - 1
    # end = queries[position][1] -1
    # while position < length:
    #     if start <= end:
    #         array[start] += queries[position][2]
    #         start += 1
    #     else:
    #         position += 1
    #         if position < length:
    #             start = queries[position][0] -1
    #             end = queries[position][1] -1
    # end_time = time.time()
    # print(end_time - start_time)
    # return max(array)



    # ---- 8.05 seconds-----#
    # arr_dict = {}
    # for idx, i in enumerate(array):
    #     arr_dict[idx] = i
    # for i in queries:
    #     start = i[0] - 1
    #     end = i[1] -1
    #     val = i[2]
    #     for i in arr_dict:
    #         if i >= start and i <= end:
    #             arr_dict[i] = arr_dict[i] + val
    # end_time = time.time()
    # print(end_time - start_time)
    # return max(arr_dict.values())


    #------9.97 seconds------#
    # for i in queries:
    #     start = i[0] -1
    #     end = i[1] -1
    #     value = i[2]
    #     for idx, i in enumerate(array):
    #         if idx >= start and idx <= end:
    #                 array[idx] = i + value
    # end_time = time.time()
    # print(end_time - start_time)
    # return max(array)

print(arrayManipulation(4000, data))