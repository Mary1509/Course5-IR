import os
import getopt
from sys import argv

from list import SortedLinkedList

node_list = SortedLinkedList()
filenames = []

index = 'results/index'
names = 'results/filenames'


def print_usage():
    print("Usage:")
    print("python query.py <word> [-i <index> -n <filenames> -h <help>]")


def search_in_index(word):
    if os.path.exists(index) and os.path.exists(names):
        print('Loading index...')
        load_index(index, names)
        print('Searching...')
        result = []
        res_node = node_list.search(word)
        if res_node:
            for el in res_node.freq:
                if el != 0:
                    result.append((el, filenames[res_node.freq.index(el)]))
            for res in result:
                print(res[0], res[1])
        else:
            print('Not found in index')
            exit(0)
    else:
        if not os.path.exists(index):
            raise FileExistsError(index)
        else:
            raise FileExistsError(names)


def load_index(index, names):
    with open(names, 'r') as fd:
        files = fd.readlines()
        for name in files:
            name = name.replace('\n', '')
            filenames.append(name)
    node_list.load_from_file(index, filenames)


if __name__ == '__main__':
    word = argv[1]
    options, arg = getopt.getopt(argv[2:], 'hi:n:', ['index',
                                                     'names',
                                                     'help'
                                                     ])

    for opt, arg in options:
        if opt == '-h':
            print_usage()
            exit(0)
        elif opt in ('-i', '--index'):
            index = arg
        elif opt in ('-n', '--filenames'):
            names = arg

    print('Searching for: ', word)
    print('Using index: ', index)

    try:
        search_in_index(word)
    except (FileExistsError, FileNotFoundError) as e:
        print('No such file or directory')
        print(e)
        exit(1)
