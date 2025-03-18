def nearly_equal(a, b):
    if len(a) != len(b):
        return False
    return sum(1 for x, y in zip(a, b) if x != y) == 1

print(nearly_equal("cat", "bat"))  # True
print(nearly_equal("cat", "dog"))  # False
