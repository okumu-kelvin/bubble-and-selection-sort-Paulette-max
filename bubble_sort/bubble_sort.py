def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort
    for n in range(len(unsorted_list) - 1, 0, -1):

        swapped = False

        for i in range(n):
            if unsorted_list[i] > unsorted_list[i + 1]:
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
                swapped = True
        if not swapped:
            break
        
    pass
