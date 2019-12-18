import math

class Node(object):
    
    def __init__(self, order):
        self.order = order
        self.keys = []
        self.values = []
        self.leaf = True

    def add(self, key, value):

        if not self.keys:
            self.keys.append(key)
            self.values.append([value])
            return None

        for i, item in enumerate(self.keys):
            if key == item:
                self.values[i].append(value)
                break

            elif key < item:
                self.keys = self.keys[:i] + [key] + self.keys[i:]
                self.values = self.values[:i] + [[value]] + self.values[i:]
                break

            elif i + 1 == len(self.keys):
                self.keys.append(key)
                self.values.append([value])
                break

    
    def split(self):

        left = Node(self.order)
        right = Node(self.order)
        mid = self.order / 2
        
        left.keys = self.keys[:math.ceil(mid)]
        left.values = self.values[:math.ceil(mid)]

        right.keys = self.keys[math.ceil(mid):]
        right.values = self.values[math.ceil(mid):]

        self.keys = [right.keys[0]]
        self.values = [left, right]
        self.leaf = False

    def is_full(self):
        return len(self.keys) == self.order

    def show(self, counter=0):

        print ("| ", counter, " | ", str(self.keys))

        if not self.leaf:
            for item in self.values:
                item.show(counter + 1)                
