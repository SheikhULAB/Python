def power_set_iterative(s):
    power_set = [[]]
    for elem in s:
        for sub_set in power_set[:]:
            power_set.append(sub_set + [elem])
    return power_set

input_set = [1, 2, 3]

print("Power set (iterative):", power_set_iterative(input_set))        