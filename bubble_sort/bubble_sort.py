def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort
    n = len(unsorted_list)
    for i in range(n):

        swapped = False

        for p in range(0, n - i -1):
            if unsorted_list[p] > unsorted_list[p + 1]:
                unsorted_list[p], unsorted_list[p + 1] = unsorted_list[p + 1], unsorted_list[p]
                swapped = True
        if not swapped:
            break
    return unsorted_list
