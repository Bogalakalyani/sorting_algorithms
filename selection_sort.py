def selection_sort(sequence):
    for i in range(len(sequence) - 1):
        minimum = i
        for j in range(i+1,len(sequence)):
            if sequence[j] < sequence[minimum]:
                minimum = j

        if i != minimum:
            sequence[minimum],sequence[i] = sequence[i],sequence[minimum]

    return sequence

print(selection_sort([1,5,6,7,4,3,9,0]))