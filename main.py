with open("in.txt") as in_file:
	lines = in_file.readlines()[::-1]
	out_file = open("out.txt", "w")
	for line in lines:
		out_file.write(line + "\n")
	out_file.close()
