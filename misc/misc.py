# Given an array of "array range", return an optimized array by deleting subarrays.
#
# NOTE: Array range (2,6) represents (2,3,4,5,6)
#
# INPUT: [(2,6),(3,5),(7,21),(20,21)]
# OUTPUT: [(2,6),(7,21)]
#
# Reason: (3,5) is a subarray of (2,6) and (20,21) is a subarray of (7,21)

def arrayRange(ranges):
    res = []
    sorted_by_first = sorted(ranges, key=lambda tup: tup[0])
    res.append(sorted_by_first[0])
    for i in range(1, len(sorted_by_first)):
        # If it fits in the previous, remove it
        if sorted_by_first[i][1] <= sorted_by_first[i-1][1]:
            continue
        else:
            res.append(sorted_by_first[i])
    return res

print arrayRange([(2,6),(3,5),(7,21),(20,21)])
print arrayRange([(3,7),(2,8),(4,5),(9,20)])
