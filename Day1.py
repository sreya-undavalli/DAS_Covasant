# Given dictionaries
D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new': 3}

# Union of keys (value does not matter)
D_UNION = {**D1, **D2}

# Intersection of keys (value does not matter)
D_INTERSECTION = {key: D1[key] for key in D1 if key in D2}

# D1 - D2 (keys in D1 but not in D2)
D1_minus_D2 = {key: D1[key] for key in D1 if key not in D2}

# Merge values for same keys (add values for same keys)
D_MERGE = {key: D1.get(key, 0) + D2.get(key, 0) for key in set(D1) | set(D2)}

# Printing the results
print("D_UNION:", D_UNION)
print("D_INTERSECTION:", D_INTERSECTION)
print("D1 - D2:", D1_minus_D2)
print("D_MERGE:", D_MERGE)
