a = {1: [0, ['G', 'C', 'P']], 2: [0, ['P', 'P', 'P']], 3: [1, ['C', 'C', 'C']], 4: [0, ['P', 'P', 'C']]}

print(sorted(a.items(), key=lambda x: x[1][0], reverse=True))
