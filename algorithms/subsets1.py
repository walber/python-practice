
def helper(given, subset, i):
    if i == len(given):
        print_subset(subset)
    else:
        subset[i] = None
        helper(given, subset, i + 1)
        subset[i] = given[i]
        helper(given, subset, i + 1)

def subsets(given):
    helper(given, [None] * len(given), 0)

def print_subset(subset):
    print(list(filter(lambda x : x is not None, subset)))

if __name__ == '__main__':
    subsets(['A', 'B', 'C', 'D'])