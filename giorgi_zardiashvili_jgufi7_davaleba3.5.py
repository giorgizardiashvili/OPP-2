j_list = [3432, 1231, 23, 543, 9684, 21, 32, 23, 24]


def max(x):
    list = []
    while x:
        minimum = x[0]
        for i in x:
            if i < minimum:
                minimum = i
        list.append(minimum)
        x.remove(minimum)
    return list[-2]


print(max(j_list))
