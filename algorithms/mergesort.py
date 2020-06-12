
def mergesort(arr):
    def merge(arr_l, arr_r):

        sorted_arr = []
        L, R = len(arr_l), len(arr_r)
        l = r = 0

        while l < L and r < R:
            if arr_l[l] < arr_r[r]:
                sorted_arr.append(arr_l[l])
                l += 1
            else:
                sorted_arr.append(arr_r[r])
                r += 1

        sorted_arr.extend(arr_l[l:L])
        sorted_arr.extend(arr_r[r:R])

        return sorted_arr
        

    def sort(arr, lb, ub):
         
        if  lb == ub:
            return [arr[lb]]

        mid = (lb + ub) // 2
        l = sort(arr, lb, mid)
        r = sort(arr, mid + 1, ub)

        return merge(l, r)

    return sort(arr, 0, len(arr) - 1) if len(arr) > 0 else arr

    



