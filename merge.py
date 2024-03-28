def merge(array):
    if len(array) == 1:
        return array
    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]
    left_half = merge(left)
    right_half = merge(right)
    return merge_sort(left_half, right_half)
def merge_sort(left, right):
    result = []
    l,r = 0,0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            print("left", result, left[l], right[r])
            l += 1
        else:
            result.append(right[r])
            print("right",result, left[l], right[r])
            r += 1
    result.extend(left[l:]) 
    print("\t\t\tresult after left extend", result)
    result.extend(right[r:])
    print("\t\t\tresult after right extend", result)
    return result
array1 = [2,8,9,3,5,4,1,7]
print(merge(array1))