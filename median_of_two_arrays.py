# Find the median of two sorted arrays.

# Time Complexity: O (n/2)
def median(arr1: list[int], arr2: list[int]) -> float:
    pt1, pt2, count = 0, 0, 0
    total_length = len(arr1) + len(arr2)
    low_mid, high_mid = -1, -1

    while pt1 < len(arr1) or pt2 < len(arr2):

        if total_length % 2 == 0 and count == total_length // 2 - 1:
            low_mid = min(arr1[pt1], arr2[pt2])

        if total_length % 2 == 0 and count == (total_length // 2):
            high_mid = min(arr1[pt1], arr2[pt2])
            return (high_mid + low_mid) / 2

        if total_length % 2 != 0 and count == total_length // 2:
            return min(arr1[pt1], arr2[pt2])

        if pt1 >= len(arr1):
            pt2 += 1
            continue

        if pt2 >= len(arr2):
            pt1 += 1
            continue

        if arr1[pt1] < arr2[pt2]:
            pt1 += 1
        else:
            pt2 += 1

        count += 1


arr1 = [0, 0, 0, 0, 1, 3, 5]
arr2 = [2, 4, 6, 7, 8]

print(median(arr1, arr2))