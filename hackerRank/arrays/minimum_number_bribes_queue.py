

# testing_arr = [1,4,6,2,3,9,5,8,7,12,10,11]
# testing_arr.sort()
# print(testing_arr)
# def minimumBribes(q):
#     bribes = 0
#     chaotic = False
#     for idx, i in enumerate(q):
#         if idx == i - 1:
#             continue
#         if (i - 1) - idx > 2:
#             chaotic = True
#         if (i - 1) - idx > 1:
#             bribes += 2
#         else:
#             bribes += 1
#     if chaotic:
#         print('Too chaotic')
#     else:
#         print(bribes)

def minimumBribes(q):
    moves = 0
    chaotic = False
    for pos, val in enumerate(q):
        if (val - 1) - pos > 2:
            chaotic = True
        for j in range(max(0, val - 2), pos):
            if q[j] > val:
                moves += 1
    if chaotic:
        print('Too chaotic')
    else:
        print(moves)

    # count = 0
    # position = len(q) - 1
    # arr = []
    # for i in q:
    #     arr.append(i - 1)
    # while position >= 0:
    #     if arr[position] is not position:
    #         if arr[position -1] == position:
    #             temp = arr.pop(position - 1)
    #             arr.insert(position, temp)
    #             count += 1
    #             position -= 1
    #         elif arr[position - 2] == position:
    #             temp = arr.pop(position -2)
    #             arr.insert(position, temp)
    #             count += 2
    #             position -= 1
    #         else:
    #             # print(len(test_arr))
    #             # print(position)
    #             print('Too chaotic')
    #             return
    #     else:
    #         position -= 1
    # print(count)




# minimumBribes(testing_arr)
minimumBribes([1,2,5,3,7,8,6,4])
minimumBribes([5, 1, 2, 3, 7, 8, 6, 4])