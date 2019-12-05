import sys
sys.path.append('.')

from src.loopqueue import LoopQueue


if __name__ == '__main__':
    test = LoopQueue()

    elems = [i for i in range(40)]
    for elem in elems:
        test.enqueue(elem)
    test.printLoopQueue()
    for i in range(37):
        test.dequeue()
    test.printLoopQueue()