def compress_text(x):
	count = 1
	i = None
	compressed_text = ""
	if len(x) > 1:
		for i in range(1, len(x)):
			if x[i - 1] == x[i]:    # if previous char equals current char
				count += 1			# increase counter
			else:
				compressed_text += x[i - 1] + str(count)  # prints char and its count
				count = 1
		compressed_text += (x[i]+ str(count))    # prints char and its count
	else:
		i = 0
		compressed_text += (x[i] + str(count))   # prints char and its count
	return compressed_text


# noinspection SpellCheckingInspection
print(compress_text("aaavvvfdff"))
