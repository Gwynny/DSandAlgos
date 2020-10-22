def MergeSortedArrays(first_list, second_list):
    """[0,3,4,31], [3,4,6,30] -> [0,3,3,4,4,6,30,31]"""

    if not (isinstance(first_list, list) and isinstance(second_list, list)):
        raise TypeError("Incorrect Input")

    if first_list == []:
        return second_list

    if second_list == []:
        return first_list

    i = 0
    j = 0
    merged_list = []
    while i < len(first_list) and j < len(second_list):
        if first_list[i] < second_list[j]:
            merged_list.append(first_list[i])
            i += 1
        else:
            merged_list.append(second_list[j])
            j += 1

    return merged_list + first_list[i:] + second_list[j:]

