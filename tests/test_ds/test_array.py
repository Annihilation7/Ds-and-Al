import sys
sys.path.append('.')

from src.ds.array import Array

if __name__ == '__main__':
    test = Array()
    print(test.getSize())
    print(test.isEmpty())

    # 插入[3, 4, 5]
    for elem in [3, 4, 5]:
        test.add(0, elem)
    test.printArray()
    # get
    print(test.get(1))
    # set
    test.set(2, 'hello')
    test.printArray()
    # contains
    print(test.contains(5))
    # find
    print(test.find('hello'))
    # remove
    test.remove(1)
    test.printArray()
    # removeElement
    test.removeElement('hello')
    test.printArray()
    # 扩容操作
    for i in range(10):
        test.add(0, i)
    test.printArray()