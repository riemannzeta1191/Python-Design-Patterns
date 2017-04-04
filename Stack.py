class ArrayStack(object):
    """ LIFO Stack implementation using a Python list as underlying storage.Adapter Pattern """


    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data)== 0

    def _push(self,x):
        return self._data.append(x)

    def _pop(self):
        if self.is_empty():
            raise ("Stack is empty")
        return self._data.pop()

    def _top(self):
        if self.is_empty():
            raise ("Stack is empty")
        return self._data[-1]

    
abc = ArrayStack()
abc._push('k')
abc._push('l')
abc._pop()
print  abc.__dict__
print len(abc)