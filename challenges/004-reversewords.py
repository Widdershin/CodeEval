# https://www.codeeval.com/open_challenges/8/

import sys

def reverse_words(sentence):
    return " ".join(reversed(sentence.split()))

def main():

    file_name = sys.argv[1]
    with open(file_name) as open_file:
        for line in open_file.readlines():
            print reverse_words(line)

if __name__ == '__main__':
    main()