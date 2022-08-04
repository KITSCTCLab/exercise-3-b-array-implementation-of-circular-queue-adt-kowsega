class MyCircularQueue:
    def __init__(self, size: int):
        # Write code here
        self.size = size
        self.lst = [None]*size
        self.queue = [None]*size
        self.top = -1
        self.rear = -1
        self.front = -1

    def enqueue(self, value: int) -> bool:
        # Write code here
        if self.top == -1:
            return 1
        else :
            return 0
        
    def dequeue(self) -> bool:
        # Write code here
        if self.front==-1 or self.front>self.rear:
            return 1
        else:
            return 0
    def get_front(self) -> int:
        # Write code here
        if self.front==-1 or self.front>self.rear:
            return 1
        else:
            return 0
    def get_rear(self):
        # Write code here
        if self.front==-1 or self.front>self.rear:
            return 1
        else:
            return 0
    def is_empty(self):
        # Write code here
        if self.front==-1 or self.front>self.rear:
            return 1
        else:
            return 0
            def is_full(self):
        # Write code here


# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
data = []
for item in input().split(','):
    item = item.strip()
    if item == '-':
        data.append([])
    else:
        data.append([int(item)])
obj = MyCircularQueue(data[0][0])
result = []
for i in range(len(operations)):
    if i == 0:
        result.append(None)
    elif operations[i] == "enqueue":
        result.append(obj.enqueue(data[i][0]))
    elif operations[i] == "get_rear":
        result.append(obj.get_rear())
    elif operations[i] == "get_front":
        result.append(obj.get_front())
    elif operations[i] == "dequeue":
        result.append(obj.dequeue())
    elif operations[i] == "is_full":
        result.append(obj.is_full())
    elif operations[i] == "is_empty":
        result.append(obj.is_empty())

print(result)
