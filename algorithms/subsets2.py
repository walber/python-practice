
def helper(given, subset, p):
    for i in range(p, len(given)):
        helper(given, subset + [given[i]], i + 1)
    
    print(subset)

def subsets(given):
    return helper(given, [], 0)

if __name__ == "__main__":
    subsets(['A', 'B', 'C', 'D'])