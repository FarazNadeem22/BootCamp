def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            print(f"{target} found at position {i}")
            return i
    print(f"{target} not found")
    return -1


my_list = [6, 3, 2, 2, 5, 7]
linear_search(my_list, 5)
linear_search(my_list, 7)
linear_search(my_list, 9)
