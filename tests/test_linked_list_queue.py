# -*- coding: utf-8 -*-
# Email: mazhenyu@datagrand.com
# Created: 2019-12-07 12:57pm


from src.linked_list_queue import LinkedListQueue


if __name__ == '__main__':
    test = LinkedListQueue()

    elems = [i for i in range(20)]
    # enqueue
    for elem in elems:
        test.enqueue(elem)
    test.print()
    # dequeue, to empty
    for i in range(20):
        test.dequeue()
    test.print()
    # enqueue
    for elem in elems:
        test.enqueue(elem)
    test.print()