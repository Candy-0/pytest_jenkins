data = {
    'test_001': {'a': 1, 'b': 2, 'c': 3},
    'test_002': {'a': 2, 'b': 3, 'c': 5},
    'test_003': {'a': 4, 'b': 5, 'c': 6}
}

print(data.values())
data_l = []
for i in data.values():
    data_l.append(tuple(i.values()))
print(data_l)
