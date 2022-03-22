
def subsets(given):
    subset = []
    for i in range(2 ** len(given)):
        for j, e in enumerate(given):
            if i & (1 << j):
                subset.append(e)

        print(subset)
        subset.clear()

if __name__ == "__main__":
    subsets(['A', 'B', 'C', 'D'])