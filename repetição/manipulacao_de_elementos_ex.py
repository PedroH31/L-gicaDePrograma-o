lst = [-2, 0, 4, 5, 1, 2]


for idx in range(len(lst) - 1):
    current_item = lst[idx]
    next_item = lst[idx + 1]

    sum_of_items = current_item + next_item
    print(sum_of_items)
