


def min_max(l):
    if l == []:
        return ('value error')
    else:
        t = (min(l) , max(l))
    return t

print (min_max([3, -1, 5, 5, 0]))
print (min_max([42]))
print (min_max([-5, -2, -9]))
print (min_max([]))
print (min_max([1.5, 2, 2.0, -3.1]))

print('_______________')

def unique_sorted(l):
    t = sorted(list(set(l)))
    return t

print (unique_sorted([3, 1, 2, 1, 3]))
print (unique_sorted([]))
print (unique_sorted([-1, -1, 0, 2, 2]))
print (unique_sorted([1.0, 1, 2.5, 2.5, 0]))
