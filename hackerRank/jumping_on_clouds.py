# input is the number of clouds that can be jumped on
#

def jumpingOnClouds(c):
    jumps = 0
    current = 0
    print(len(c))
    length = len(c) - 1
    while current < length:
        if current + 2 < length:
            if c[current + 2] == 0:
                current += 2
                jumps += 1
            elif current + 1 < length:
                if c[current + 1] == 0:
                    current += 1
                    jumps += 1
        else:
            current += 2
            jumps += 1
        # if current + 1 < length and current + 2 < length:
        #     if c[current + 1] == 0 and c[current + 2] == 0:
        #         current = current + 2
        #         jumps += 1
        # if c[current + 1] == 0:
        #     current += 1
        #     jumps += 1
        # else:
        #     current = current + 2
        #     jumps += 1
    return jumps

print(jumpingOnClouds([0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0]))
# print(jumpingOnClouds([0,0,0,1,0,0]))