# merge sorted lists

l1 = list(range(1,10,2))
l2 = list(range(0,10,2))
l2.extend([11, 12, 13])
print(l1)
print(l2)

def merge_sorted_lists(lst1, lst2):
    lst = []
    ix, ix1, ix2 = 0, 0, 0
    while ix1 < len(lst1) and ix2 < len(lst2):
        if lst1[ix1] < lst2[ix2]:
            lst.append(lst1[ix1])
            ix1 += 1
        else:
            lst.append(lst2[ix2])
            ix2 += 1
        ix += 1
    while ix1 < len(lst1):
        lst.append(lst1[ix1])
        ix1 += 1
    while ix2 < len(lst2):
        lst.append(lst2[ix2])
        ix2 += 1
    return lst

l = merge_sorted_lists(l1, l2)
print(l)
