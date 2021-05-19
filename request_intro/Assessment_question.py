t = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def find_index_odd_even(sought_list, val2):
    index = sought_list.index(val2)
    if index % 2 == 0:
        return True
    else:
        return False
