
# def recusiveFunc(ammtLeft, cost, freeContainer):
#     containers = ammtLeft // cost
#     if containers >= freeContainer:
#         numberOfFreeConatiners = containers // freeContainer
#         totalOfFreeConatiners = freeContainer * numberOfFreeConatiners
#         leftOver = containers - totalOfFreeConatiners
#         ammtLeftOver = leftOver + totalOfFreeConatiners
#         recusiveFunc(ammtLeftOver, cost, freeContainer)
#     else:
#         return containers
def maximumContainers(scenarios):
   for i in scenarios:
       subArray = i.split(' ')
       budget =  int(subArray[0])
       cost = int(subArray[1])
       free = int(subArray[2])

       total = budget // cost

       leftover = total
       while leftover >= free:
           a = leftover // free
           total += a
           b = a * free
           leftover = leftover - b + a
       print(total)




print(maximumContainers(['10 2 5', '12 4 4', '6 2 2']))