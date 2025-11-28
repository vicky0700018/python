def print_table(n, upto=10):
	for i in range(1, upto + 1):
		print(f"{n} x {i} = {n * i}")


if __name__ == "__main__":
	# Print table of 13
	print_table(13, upto=10)