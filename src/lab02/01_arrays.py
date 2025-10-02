from turtledemo.sorting_animate import instructions1


def min_max(nums):
    if nums == []:
        return ('value error')
    else:
        t = (min(nums) , max(nums))
    return t



def unique_sorted(nums):
    t = sorted(list(set(nums)))
    return t

def flatten(mat):
    t = list ()
    for i in mat:
        if type(i) == list or type(i) == tuple:
            t.extend(i)
        else:
            return ('TypeError')
    return (t)

        #if type(i) == list:

        #else:
         #   return ('value error')

print (min_max([3, -1, 5, 5, 0]))
print (min_max([42]))
print (min_max([-5, -2, -9]))
print (min_max([]))
print (min_max([1.5, 2, 2.0, -3.1]))
print('_______________')
print (unique_sorted([3, 1, 2, 1, 3]))
print (unique_sorted([]))
print (unique_sorted([-1, -1, 0, 2, 2]))
print (unique_sorted([1.0, 1, 2.5, 2.5, 0]))
print('_______________')
print (flatten([[1, 2], [3, 4]]))
print (flatten([[1, 2], (3, 4, 5)]))
print (flatten([[1], [], [2, 3]]))
print (flatten([[1, 2], "ab"]))