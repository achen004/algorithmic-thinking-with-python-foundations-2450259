#selection sort algo

def selection_sort(some_list):
    for i in range(len(some_list)-1):
        min_index=i
        for j in range(i+1, len(some_list)):
            if some_list[min_index]>some_list[j]:
                some_list[min_index], some_list[j]=some_list[j], some_list[min_index]
    return some_list

some_list=[3, 2, 1, 5, 4]
selection_sort(some_list)

#pythonic way to check if list sorted; not built in
print(all(some_list[i] <= some_list[i+1] for i in range(len(some_list)-1)))
