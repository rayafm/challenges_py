def deduplicate_lists(lst1, lst2, reverse=False):
    merged_lst = lst1 + lst2
    lst = []
    reversed_lst = []

    for ls in merged_lst:
        if ls not in lst:
            lst.append(ls)

    sorted_lst = sorted(lst)

    if reverse==True:
        for i in range(len(sorted_lst)-1, -1, -1):
            reversed_lst.append(sorted_lst[i])
        return reversed_lst
    else:
        return sorted_lst