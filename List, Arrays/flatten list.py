def flatten(lol):
    flatlist = []
    for element in lol:
        if type(element) is list:
            for item in element:
                flatlist.append(item)
        else:
            flatlist.append(element)
    return flatlist

nestedlist = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
print("This is the flat list", flatten(nestedlist))
