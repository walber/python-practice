from random import choice

def quicksort(arr):
    def partition(arr, l, r):
        item = choice(arr[l:r + 1])

        while l <= r:
            while arr[l] < item:
                l += 1

            while arr[r] > item:
                r -= 1

            if l <= r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        return l

    """
    def sort(arr, lb, ub):
        if lb < ub:
            i = partition(arr, lb, ub)
            sort(arr, lb, i - 1)
            sort(arr, i, ub)
    """
    def sort(arr, lb, ub):
        stk = [(lb, ub)]

        while stk:
            l, r = stk.pop()

            if l < r:
                i = partition(arr, l, r)
                stk.append((l, i - 1))
                stk.append((i, r))

    return sort(arr, 0, len(arr) - 1)

