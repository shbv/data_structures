# List defs
def foo():
    pass
l = [2, 'test', 5.0, foo]
l.append(10)
l.insert(0, 't1')    # insert at index 0
l.remove('test')     # remove element 'test'
l.pop()              # return/remove last element
l.pop(-1)            # return/remove index -1
l.reverse()
l[1:5:2]             # elements from index 1 through 4 in steps of 2
l[2:-1]
del l[1:3]

