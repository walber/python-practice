
def kadene(arr):
    max_glob = arr[0]
    max_curr = arr[0]
    bounds = (0, 1)
    lb = bounds[0]

    for i in range(1, len(arr)): 
        if arr[i] >= (max_curr + arr[i]):
            max_curr = arr[i]
            lb = i 
        else:
            max_curr = max_curr + arr[i]
            lb = bounds[0]

        if max_curr > max_glob:
            max_glob = max_curr
            bounds = (lb, i + 1)

    lb, ub = bounds
    return arr[lb:ub]
