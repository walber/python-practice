
def mergesort(arr):
    def merge(arr, lb, mid, ub):

        helper_arr = arr[lb:ub + 1]
        curr = l = lb
        r = mid + 1

        while l <= mid and r <= ub:
            if helper_arr[l - lb] < helper_arr[r - lb]:
                arr[curr] = helper_arr[l - lb]
                l += 1
            else:
                arr[curr] = helper_arr[r - lb]
                r += 1
            curr +=1

        for i in range(l, mid + 1):
            arr[curr] = helper_arr[i - lb]
            curr += 1
        

    def sort(arr, lb, ub):

        if lb < ub:
            mid = (lb + ub) // 2
            sort(arr, lb, mid)
            sort(arr, mid + 1, ub)
            merge(arr, lb, mid, ub)


    return sort(arr, 0, len(arr) - 1)
    



