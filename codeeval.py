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
\"\"\"
"""

INPUT_CONTENTS = """
###### IO Boilerplate ######
import sys

if len(sys.argv) < 2:
    input_file_name = "{}"
else:
    input_file_name = sys.argv[1]

with open(input_file_name) as input_file:
    input_lines = map(lambda x: x.strip(), filter(lambda x: x != '', input_file.readlines()))

###### /IO Boilerplate ######

"""

DEFAULT_CODE = """
def main():
    pass


if __name__ == '__main__':
    main()
"""

def format_example(ex):
    output = ""
    for line in ex.split('\n'):
        output += "\n    {}".format(line)

    output += "\n"

    return output


def main():
    os.chdir('challenges')
    generated_url = URL(index)
    request = requests.get(generated_url)
    soup = BeautifulSoup(request.text)

    content = soup.find(id='requisition')

    tags = content.find_all(['p', 'pre'])

    def pop_tag(tags):
        return tags.pop(0).text

    description = pop_tag(tags)
    input_desc = pop_tag(tags)

    input_ex = ""
    if tags[0].name == "pre":
        input_ex = pop_tag(tags)
        input_desc += format_example(input_ex)

    output_desc = pop_tag(tags)

    if tags[0].name == "pre":
        output_desc += format_example(pop_tag(tags))

    title = content.h2.text

    stripped_name = title.strip().lower().replace(' ', '')

    files = os.listdir('.')

    valid_files = []
    for fname in files:
        try:
            fname_prefix = fname[:fname.index('-')]
        except ValueError:
            continue

        if fname_prefix.isdigit():
            valid_files.append(int(fname_prefix))
    prefix = max(valid_files) + 1

    prefix = str(prefix).zfill(3)

    
    file_name = "{}-{}.py".format(prefix, stripped_name)
    if input_ex:
        input_ex_file_name = "{}-{}-in.txt".format(prefix, stripped_name)

    with open(file_name, 'w') as open_file:
        open_file.write(FILE_CONTENTS.format(url=generated_url, title=title, challenge=description, input_desc=input_desc, output_desc=output_desc))

        if input_ex:
            open_file.write(INPUT_CONTENTS.format(input_ex_file_name))

        open_file.write(DEFAULT_CODE)

    if input_ex:        
        with open(input_ex_file_name, 'w') as input_file:
            input_file.write(input_ex.strip())

if __name__ == '__main__':
    main()