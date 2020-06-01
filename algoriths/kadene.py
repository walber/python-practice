
def Kadene(arr):
    max_glob = arr[0]
    max_curr = arr[0]
    bounds = (0, 1)

    for i in range(1, len(arr)): 
        if arr[i] >= (max_curr + arr[i]):
            max_curr = arr[i]
            new_bounds = (i, i + 1)
        else:
            max_curr = max_curr + arr[i] 
            new_bounds = (bounds[0], i + 1)

        if max_curr > max_glob:
            max_glob = max_curr
            bounds = new_bounds

    lb, ub = bounds
    return arr[lb:ub]
