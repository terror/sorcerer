def get_slice_length(path):
    for i in range(len(path)):
        if path[i].isalpha():
            return i
    return -1
