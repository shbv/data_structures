# Remove even numbers from list

l = list(range(10))
print(l)

def remove_even(lst):
    return [el for el in lst if el%2 !=0]

l = remove_even(l)
print(l)
