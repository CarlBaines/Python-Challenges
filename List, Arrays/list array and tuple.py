names = ['List','Array','Tuple']
mut = ['Yes', 'Yes', 'No']
csize = ['No', 'No', 'No']
citems = ['Yes', 'Yes', 'No']
dt = [3, 1, 1]

titles = ['names', 'mut', 'csize', 'citems','dt']
data = [titles] + list(zip(names, mut, csize, citems, dt))

for i, d in enumerate(data):
    l = 'l'.join(str(x).ljust(12) for x in d)
    print(line)
    if i == 0:
        print('-' * len(l))
