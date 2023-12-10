# time complexity = best_case : 0(n) worst_case :0(n^2)
# space complexity =  0(1)

def bubble_sort(sequence):
    length = len(sequence) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0,length):
            if sequence[i] > sequence[i + 1]:
                sorted = False
                sequence[i],sequence[i+1] = sequence[i+1],sequence[i]

    return sequence


print(bubble_sort([1,3,5,2,3,9,8,0,7,6,5,4,0]))

