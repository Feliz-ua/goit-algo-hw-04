def merge(left, right):
    merged = []
    Left_index =0
    Right_index =0
    
    while Left_index < len(left) and Right_index < len(right):
        if left[Left_index] <= right[Right_index]:
            merged.append(left[Left_index])
            Left_index += 1
        else:
            merged.append(right[Right_index])
            Right_index += 1
    merged.extend(left[Left_index:])
    merged.extend(right[Right_index:])
    return merged


def merge_k_lists(lists):
    result = []
    for lst in lists:
        result = merge(result, lst)  # використовуємо merge з merge_sort
    return result


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)
    # Відсортований список: [1, 1, 2, 3, 4, 4, 5, 6]
