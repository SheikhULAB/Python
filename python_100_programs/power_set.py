from itertools import chain, combinations

def power_set(s):
    return list(chain.from_iterable(combinations(s,r) for r in range(len(s) + 1)))

input_set = [1,2,3]

print("Power Set: ", power_set(input_set))