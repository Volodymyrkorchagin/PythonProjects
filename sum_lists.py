def sum_lists(list1, list2):
    n = max(len(list1), len(list2))

    for i in range(n):
        a = list1[i] if i < len(list1) else 0
        b = list2[i] if i < len(list2) else 0
        yield a + b