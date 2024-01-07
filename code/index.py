import os
import re
from sys import argv
import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords')

from list import Node, SortedLinkedList

node_list = SortedLinkedList()
filenames = []


def print_usage():
    print("Usage:")
    print("python index <filename>")


def create_index(filename):
    print(f"Indexing file {filename}...")
    stop_words = set(stopwords.words('english'))
    with open(filename, 'r') as fd:
        for line in fd.readlines():
            line = line.strip()
            line = re.sub(r'[^\w\s]', '', line)
            line = line.lower()
            line = line.split()
            filtered = [w for w in line if not w in stop_words]
            for word in filtered:
                if node_list.search(word):
                    word_node = node_list.search(word)
                    word_node.freq[filenames.index(filename)] += 1
                else:
                    word_node = Node(word, filenames)
                    word_node.freq[filenames.index(filename)] += 1
                    node_list.insert(word_node)

        node_list.display()


def save_index():
    with open('results/filenames', 'w') as fd:
        for filename in filenames:
            fd.writelines(filename + '\n')
    node_list.save_to_file('results/index')


if __name__ == '__main__':
    n = len(argv)
    if n < 2:
        print("Not enough arguments")
        print_usage()
        exit(1)
    if n > 2:
        print("Too many arguments")
        print_usage()
        exit(1)

    try:
        inputfile = argv[1]
        if os.path.exists(inputfile):
            if os.path.isdir(inputfile):
                dir_filenames = os.listdir(inputfile)
                for filename in dir_filenames:
                    file = os.path.abspath(os.path.join(inputfile, filename))
                    filenames.append(file)
                for filename in filenames:
                    create_index(filename)
            elif os.path.isfile(inputfile):
                filenames.append(inputfile)
                create_index(inputfile)
            else:
                raise FileNotFoundError(inputfile)
            save_index()
        else:
            raise FileExistsError(inputfile)
    except (FileExistsError, FileNotFoundError) as e:
        print('No such file or directory')
        print(e)
        exit(1)
