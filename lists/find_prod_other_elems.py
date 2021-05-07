# Create list with product of all elements except itself
l = list(range(1,6))
print(l)

def find_product_other_elems(lst):

    product_lst = [] # compute left products and multiply with right products later

    left_product = 1 # first element has left product of 1
    for el in lst:
        product_lst.append(left_product)  
        left_product *= el # update left product for next element

    right_product = 1 # last element has right product of 1
    for ix in range(len(lst)-1, -1, -1):
        product_lst[ix] *= right_product  
        right_product *= lst[ix] # update right product for previous element

    return product_lst

print(find_product_other_elems(l))
