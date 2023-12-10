# time_complexity : worst_case = 0(n^2) best_case = 0(n)
#space_complexity : 0(1)


def insertion_sort(sequence):
    for i in range(1,len(sequence)):
        value = sequence[i]

        while i > 0 and sequence[i-1] > value:
            sequence[i-1],sequence[i] = sequence[i],sequence[i-1]
            i -=1
        
    return sequence


print(insertion_sort([1,9,8,7,5,6,4,9,8,0,4]))