import unittest
from src.ds.linked_list import LinkedList


class Test_LinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.processer = LinkedList()

    def test_all(self):
        elems = [i for i in range(30)]

        # add
        for elem in elems:
            self.processer.addFirst(elem)
        self.processer.printLinkedList()
        self.processer.add(10, 'haha')
        self.processer.printLinkedList()
        # get
        print(self.processer.get(10))
        # set
        self.processer.set(10, '?')
        self.processer.printLinkedList()
        # contains
        print(self.processer.contains('?'))
        # remove
        self.processer.remove(10)
        self.processer.printLinkedList()
        self.processer.removeFirst()
        self.processer.printLinkedList()
        self.processer.removeLast()
        self.processer.printLinkedList()
        # removeElement
        self.processer.removeElement(9)
        self.processer.printLinkedList()


if __name__ == '__main__':
    unittest.main()