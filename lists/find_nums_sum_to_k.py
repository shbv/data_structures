# Find nums in list that sum to k

l = list(range(1,10))
l.remove(8)
k = 9
print(l)
print(k)

def find_nums_sum_to_k(lst, k):
    lst.sort() # sort in ascending order
    ix1, ix2 = 0, len(lst)-1
    while ix1 != ix2:
        if lst[ix1] + lst[ix2] > k:
            ix2 -= 1
        elif lst[ix1] + lst[ix2] < k:
            ix1 += 1
        else:
            return (lst[ix1], lst[ix2])
    return False

print(find_nums_sum_to_k(l, k))

