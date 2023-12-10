# time_complexity : average: 0(nlogn) worst_case: 0(n^2)
# space_complexity : average: 0(logn) worst_case: 0(n)


def quick_sort(sequence):
    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    lesser_values = []
    greater_values = []

    for i in sequence:
        if i > pivot:
            greater_values.append(i)
        else:
            lesser_values.append(i)

    return quick_sort(lesser_values) + [pivot] + quick_sort(greater_values)


print(quick_sort([1,3,6,9,7,2,3,5,4,0,6,8,6,5]))