def find_dups(lst):
    return list(set(x for x in lst if lst.count(x) > 1))

print(find_dups([1, 2, 3, 4, 2, 3, 5]))  # [2, 3]
