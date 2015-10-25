# Random algorithms using arrays

# Given an array of n integers which has both positive and negative integers,
# sort this array such that the negative integers should in the front
# and the positive integers should in the back. The relative position should not be changed.
# eg. -1 1 3 -2 2 ans: -1 -2 1 3 2.
def putNegativesBefore(array):
    lastNegIndex = -1
    for i in range(len(array)):
        num = array[i]
        if num < 0:
            del array[i]
            array.insert(lastNegIndex + 1, num)
            lastNegIndex += 1
    return array

print putNegativesBefore([-1,1,3,-2,2])
