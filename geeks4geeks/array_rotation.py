
'''
https://www.geeksforgeeks.org/array-rotation/

Write a function rotate(ar[], d) that rotates arr[] by d elements.

arr = [1, 2, 3, 4, 5, 6, 7]
Rotation of the above array by 2 will make array like the following:
arr = [3, 4, 5, 6, 7, 1, 2]
'''

def rotate(arr, d):
    l = len(arr)
    d = d % l
    if d == l:
        return arr

    # store initial d elements
    sub_arr = []
    for i in range(d):
        sub_arr.append(arr[i])

    for i in range(l-d):
        arr[i] = arr[i+d]

    for i in range(l-d, l):
        arr[i] = sub_arr[i - (l-d)]

    return arr


arr = rotate([1, 2, 3, 4, 5, 6, 7], 2)
print(arr)
arr = rotate([1, 2, 3, 4, 5, 6, 7], 7)
print(arr)
arr = rotate([1, 2, 3, 4, 5, 6, 7], 15)
print(arr)
