

def minimumBribes(q):
    count = 0
    q_dict = {}
    for idx,item in enumerate(q):
        q_dict[item - 1] = idx
    chaotic = False
    for i in q_dict:
        print(q_dict)
        if i is not q_dict[i]:
            if i - q_dict[i] <= 2:
                temp = q_dict[i]
                q_dict[i] = q_dict[temp]
                q_dict[temp] = temp
                count += 1
            else:
                chaotic = 'Too chaotic'
                break
    if chaotic:
        print(chaotic)
    else:
        print(count)


minimumBribes([2,1,5,3,4])
minimumBribes([1,2,5,3,7,8,6,4])
minimumBribes([5, 1, 2, 3, 7, 8, 6, 4])