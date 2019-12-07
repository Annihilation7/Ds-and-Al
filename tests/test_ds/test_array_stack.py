import unittest
from src.ds.array_stack import ArrayStack


class Test_ArrayStack(unittest.TestCase):
    def setUp(self) -> None:
        self.processer = ArrayStack()

    def test_all(self):
        # push
        for i in range(20):
            self.processer.push(i)
        self.processer.printStack()
        # pop
        for i in range(5):
            self.processer.pop()
        self.processer.printStack()
        # peek
        print(self.processer.peek())


if __name__ == '__main__':
    unittest.main()