# Creating sets
set1 = {1, 2, 3, 4, 5}  # Using curly braces
set2 = set([4, 5, 6, 7, 8])  # Using set() function

# Adding elements to a set
set1.add(6)
set1.update([7, 8, 9])

# Removing elements from a set
set1.remove(5)  # Raises KeyError if element does not exist
set1.discard(10)  # Removes element if present, no error if not present

# Checking if an element is in a set
if 3 in set1:
    print("3 is in set1.")

# Union of sets
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# Difference of sets
difference_set = set1.difference(set2)
print("Difference of set1 and set2:", difference_set)

# Checking if a set is a subset or superset of another set
subset = {4, 7}
if subset.issubset(set1):
    print("subset is a subset of set1.")
if set1.issuperset(subset):
    print("set1 is a superset of subset.")

# Removing all elements from a set
set1.clear()

# Checking the length of a set
set_len = len(set2)
print("Length of set2:", set_len)
