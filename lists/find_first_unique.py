# Find first non repeating element in list

l = list(range(10))
l.extend(list(range(5)))
print(l)

# O(n**2) without using hash (hash is O(n))
def find_first_unique(lst):
    for ix1 in range(len(lst)):
        repeating = False
        for ix2 in range(len(lst)):
            if ix1!=ix2 and lst[ix1]==lst[ix2]:
                repeating = True
                break
        # if not repeating, return it
        if not repeating:
            return lst[ix1]
    return None

print(find_first_unique(l))
