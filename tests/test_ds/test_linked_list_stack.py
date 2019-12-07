import sys
sys.path.append('.')

from src.ds.linked_list_stack import LinkedListStack


if __name__ == '__main__':
    test = LinkedListStack()
    elems = [i for i in range(30)]

    # push
    for elem in elems:
        test.push(elem)
    test.print()
    # pop
    for i in range(10):
        test.pop()
    test.print()
    # peek
    print(test.peek())