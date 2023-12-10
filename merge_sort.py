# time_complexity : 0(nlogn)
# space_complexity : 0(n)

def merge_sort(sequence):
    mid = len(sequence) // 2
    if len(sequence) > 1:
        left_sequence = sequence[:mid]
        right_sequence = sequence[mid:]

        merge_sort(left_sequence)
        merge_sort(right_sequence)

        i,j,k = 0,0,0

        while i < len(left_sequence) and j < len(right_sequence):
            if left_sequence[i] < right_sequence[j]:
                sequence[k] = left_sequence[i]
                i += 1
            else:
                sequence[k] = right_sequence[j]
                j += 1
            k += 1

        while i < len(left_sequence):
            sequence[k] = left_sequence[i]
            i += 1
            k += 1

        while j < len(right_sequence):
            sequence[k] = right_sequence[j]
            j += 1
            k += 1
        
s = [8,1,3,2]
merge_sort(s)
print(s)