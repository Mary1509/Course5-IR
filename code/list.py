import json


class Node:
    def __init__(self, word, file_arr):
        self.word = word
        self.freq = [0] * len(file_arr)
        self.next = None


class SortedLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, node):
        if not self.head or node.word < self.head.word:
            node.next = self.head
            self.head = node
            return

        current = self.head

        while current.next and current.next.word < node.word:
            current = current.next

        node.next = current.next
        current.next = node

    def search(self, word):
        current = self.head
        if not current:
            return None
        while current:
            if current.word == word:
                return current
            current = current.next
        return None

    def display(self):
        current = self.head
        while current:
            print(current.word, current.freq, end='\n')
            current = current.next
        print()

    def convert_to_dict(self):
        data_dict = {}
        current = self.head

        while current:
            data_dict[current.word] = current.freq
            current = current.next

        return data_dict

    def save_to_file(self, file):
        data = self.convert_to_dict()
        with open(file, 'w') as f:
            json.dump(data, f)

    def load_from_file(self, file, filenames):
        with open(file, 'r') as f:
            data = json.load(f)
            for word in data:
                new_node = Node(word, filenames)
                new_node.freq = data[word]
                self.insert(new_node)