from itertools import product


def gen_comb_list(list_set):

    # Use itertools.product to get the Cartesian product of the input lists
    combinations = list(product(*list_set))

    # Convert each tuple in the combinations to a list
    result = [list(combination) for combination in combinations]

    return result


# Examples
print(gen_comb_list([[1, 2, 3]]))
print(gen_comb_list([[1, 2, 3], [4, 5]]))
print(gen_comb_list([[1, 2, 3], [4, 5], [6, 7, 8]]))
