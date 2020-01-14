def binarysearch(my_list, s_item, start, stop):
    if start > stop:
        return False
    else:
        middle = (start + stop) // 2
        if s_item == my_list[middle]:
            return middle
        elif s_item < my_list[middle]:
            return binarysearch(my_list, s_item, start, middle - 1)
        else:
            return binarysearch(my_list, s_item, middle + 1, stop)


my_list = [1, 2, 5, 6, 8, 10, 23, 40, 43, 45, 67, 68]
s_item = 10
start = 0
stop = len(my_list)

i = binarysearch(my_list, s_item, start, stop)

if i == -1:
    print ("Item", s_item, "not in the list")
else:
    print ("Item", s_item, "found at index", i)
