import sys

file_name = sys.argv[1]

with open(file_name) as open_file:
	for line in open_file.readlines():
		a, b, n = map(int, line.split())
		output = ""

		for i in xrange(1, n + 1):
			out = ""
			
			spacing = " "
			
			if i == 1:
				spacing = ""

			if i % a == 0:
				out += "F"

			if i % b == 0:
				out += "B"

			output += spacing + (out or str(i))

		print output
