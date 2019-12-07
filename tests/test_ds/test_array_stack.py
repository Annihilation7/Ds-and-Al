import sys 
sys.path.append('.')

from src.ds.array_stack import ArrayStack


test = ArrayStack()

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