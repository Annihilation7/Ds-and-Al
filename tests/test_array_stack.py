import sys 
sys.path.append('.')

from src.arraystack import StackArray


test = StackArray()

# push
for i in range(20):
    test.push(i)
test.printStack()
# pop
for i in range(5):
    test.pop()
test.printStack()
# peek
print(test.peek())