class MyQueue(object):
    def __init__(self):
        # we need two stacks, one will contain the "real" stack in reverse

        # real stack
        self.enqueue = []

        # reverse stack
        self.dequeue = []

    # helper method to add all ints in "real" stack, to reverse stack (in reverse order)
    def _transfer(self):
        if len(self.dequeue) == 0:
            while len(self.enqueue) > 0:
                self.dequeue.append(self.enqueue[-1])
                self.enqueue.pop()

    def peek(self):
        self._transfer()
        return self.dequeue[-1]

    # because we want o(1) pops we check if the reverse stack has ints, if it does then we pop those first, if not then we copy the enqueued objects first in reverse order and pop those while they last
    # although it is o(n) worst case, it is o(1) average case
    def pop(self):
        self._transfer()
        self.dequeue.pop()

    # main stack/enqueue will hold all values until a pop or peek is called
    def put(self, value):
        self.enqueue.append(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
