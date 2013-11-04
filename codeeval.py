"""
codeeval.py

A utility for setting up codeeval challenges.

Usage: codeeval.py <challenge index>
"""

import sys
import requests
import os
from bs4 import BeautifulSoup

URL = "https://www.codeeval.com/browse/{}/".format
index = sys.argv[1]

FILE_CONTENTS = """\"\"\"
{url}

{title}

Challenge Description:
{challenge}

Input Sample:
{input_desc}

Output Sample:
{output_desc}
\"\"\""""

def format_example(ex):
	output = ""
	for line in ex.split('\n'):
		output += "\n    {}".format(line)

	output += "\n"

	return output


def main():
	generated_url = URL(index)
	request = requests.get(generated_url)
	soup = BeautifulSoup(request.text)

	content = soup.find(id='requisition')

	description, input_desc, output_desc = map(lambda x: x.text, content.find_all('p'))

	if input_desc.strip() != "There is no input for this program.":
		input_desc += format_example(content.find_all('pre')[0].text)

	output_desc += format_example(content.find_all('pre')[-1].text)

	title = content.h2.text

	stripped_name = title.strip().lower().replace(' ', '')

	prefix = max(int(fname[0]) for fname in os.listdir('.') if fname.endswith('.py') and fname[0].isdigit()) + 1

	file_name = "{}-{}.py".format(prefix, stripped_name)

	with open(file_name, 'w') as open_file:
		open_file.write(FILE_CONTENTS.format(url=generated_url, title=title, challenge=description, input_desc=input_desc, output_desc=output_desc))

if __name__ == '__main__':
	main()