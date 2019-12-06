import sys
sys.path.append('.')

from src.linkedlist import LinkedList


if __name__ == '__main__':
    test = LinkedList()
    elems = [i for i in range(30)]

    # add
    for elem in elems:
        test.addFirst(elem)
    test.printLinkedList()
    test.add(10, 'haha')
    test.printLinkedList()
    # get
    print(test.get(10))
    # set
    test.set(10, '?')
    test.printLinkedList()
    # contains
    print(test.contains('?'))
    # remove
    test.remove(10)
    test.printLinkedList()
    test.removeFirst()
    test.printLinkedList()
    test.removeLast()
    test.printLinkedList()