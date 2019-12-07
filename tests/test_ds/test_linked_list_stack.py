import unittest
from src.ds.linked_list_stack import LinkedListStack


class Test_LinkedListStack(unittest.TestCase):
    def setUp(self) -> None:
        self.processer = LinkedListStack()

    def test_all(self):
        elems = [i for i in range(30)]

        # push
        for elem in elems:
            self.processer.push(elem)
        self.processer.print()
        # pop
        for i in range(10):
            self.processer.pop()
        self.processer.print()
        # peek
        print(self.processer.peek())


if __name__ == '__main__':
    unittest.main()