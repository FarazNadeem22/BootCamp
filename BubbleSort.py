"""Bubble Sort"""

unsorted_lst = [32, 8, 65, 55, 77, 4]


def bubblesort(lst):

    index_high = len(lst) - 1
    print(lst)

    for i in range(index_high):
        unchanged = True
        for j in range(index_high):
            item = lst[j]
            next = lst[j+1]

            if item > next:
                lst[j] = next
                lst[j+1] = item
                unchanged = False

            print(lst, i, j)


bubblesort(unsorted_lst)
