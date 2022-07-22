original_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13]]
buffer_list = []
new_list = []
for lists in original_list:
    buffer_list = lists
    for buffer_list in buffer_list:
        print(buffer_list)
    new_list.append(i)
print(new_list)
