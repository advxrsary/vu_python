def filter_list(one_d_list):
	filtered = []

	for item in one_d_list:
		if 100 >= item >= 10:
			filtered.append(item)

	mean_value = sum(filtered) / len(filtered)
	min_value = min(filtered)
	max_value = max(filtered)
	sum_of_values = sum(filtered)
	return mean_value, min_value, max_value, sum_of_values


def filter_two_d_list(two_d_list):

	for obj in two_d_list:
		filtered = filter_list(obj)
		print(filtered)


print(filter_list([1, 10, 34, 110, 400, 30, 20, 100, 101, 9, 11, 10]))
filter_two_d_list([
    [1, 10, 34, 110, 400, 30, 20],
    [-5, -10, 55, 120, 30],
    [2, 67, 23, 78, 200],
])
