#  using a graph method to count the number of cycles to figure out the minimum number of swaps

def minimumSwaps(arr):
    swaps = 0
    length = len(arr)
    array_dict = {}
    for idx,item in enumerate(arr):
        # subtracting one from each number to match index numbering of array
        array_dict[item - 1] = idx
    # create an array with false values to switch to true by index.  This defines the visited indexes
    visited = [False] * length

    # loop with the key,value in the dictionary sorted by the key in the dictionary
    # using .items() return an array of tuples with the key,value pairs
    # the key in sorted tells the sorted function what to sort by.
    # lambda represents a python anonymous function x represents each item and x[0] is the first part of the item

    for key,value in sorted(array_dict.items(), key=lambda x: x[0]):
        # check to see if the key has been visited or if the key matches the value"index"
        if visited[key] or key == value:
            # if true continue will move the loop to the next item
            continue
        cycle_count = 0
        value = key #set value to the key to check the value in the visited array with a while loop
        while not visited[value]:
            visited[value] = True # setting visited array to know that we have checked it
            value = array_dict[value] # sets the edge for the spot the value is supposed to be
            cycle_count += 1 #increment cycle count
        swaps += cycle_count - 1 #  sets the swaps to the ammout of cycles the while loop took to get back to the visited value

    return swaps
print(minimumSwaps([1,3,5,2,4,6,7]))