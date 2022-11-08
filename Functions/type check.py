def only_ints(a,b):
    if type(a) is int and type(b) is int:
        print("True")
    else:
        print("False")
    return only_ints
only_ints(12,24)
