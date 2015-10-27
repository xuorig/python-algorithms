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


# We have an array of objects A and an array of indexes B.
#Reorder objects in array A with given indexes in array B.
# Do not change array A's length.
#
# example:
#
#
# var A = [C, D, E, F, G];
# var B = [3, 0, 4, 1, 2];
#
# sort(A, B);
# // A is now [D, F, G, C, E];


def reOrderFromIndexes(orig, indexes):
    for i in range(len(orig)):
        index = indexes[i]
        orig[i], orig[index] = orig[index], orig[i]
        indexes[i], indexes[index] = indexes[index], indexes[i]
    return orig

A = ['C', 'D', 'E', 'F', 'G']
B = [3, 0, 4, 1, 2]
print(reOrderFromIndexes(A, B))

# Find the first and last occurrence of a number in a sorted array of integers
# For Example: int[] a = {1,2,3,4,5,5,7,8}

def firstAndLastOccurence(array, x):
    first = None
    last = None
    for i, elem in enumerate(array):
        if elem == x:
            if first is None:
              first = i
              end = i
            else:
              last = i
    return (first, last)

print firstAndLastOccurence([1,2,3,4,5,5,7,8], 5)
