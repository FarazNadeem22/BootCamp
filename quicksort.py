"""Quick Sort"""


def sort_part(lst, idx_low, idx_pivot):
    pivot_val = lst[idx_pivot]

    while idx_pivot != idx_low:
        low_val = lst[idx_low]

        print(lst, low_val, pivot_val)
        if low_val <= pivot_val:
            idx_low += 1
        else:
            lst[idx_low] = lst[idx_pivot-1]
            lst[idx_pivot] = low_val
            lst[idx_pivot-1] = pivot_val
            idx_pivot -= 1
    return idx_pivot


def quicksort(lst, idx_low, idx_high):

    if idx_low > idx_high:
        return

    idx_pivot = sort_part(lst, idx_low, idx_high)
    quicksort(lst, idx_low, idx_pivot-1)
    quicksort(lst, idx_high+1, idx_high)


"""Driver"""
my_list = [5, 4, 1, 2, 3]
quicksort(my_list, 0, len(my_list)-1)
print("my_list:", my_list)
