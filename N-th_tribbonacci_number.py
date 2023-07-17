def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    trib_array = [0]*(n+1)
    trib_array[1] = 1
    trib_array[2] = 1
    for i in range(3,n+1):
        trib_array[i] = trib_array[i-1] + trib_array[i-2] + trib_array[i-3]
    return trib_array[-1]