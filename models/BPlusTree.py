from models.Node import Node

class BPlusTree(object):

    # Inicializamos, por defecto en orden 4
    def __init__(self, order=4):
        self.root = Node(order)

    def _find(self, node, key):

        for i, item in enumerate(node.keys):
            if key < item:
                return node.values[i], i

        return node.values[i + 1], i + 1

    def _balance(self, parent, child, index):
      
        parent.values.pop(index)
        pivot = child.keys[0]

        for i, item in enumerate(parent.keys):
            if pivot < item:
                parent.keys = parent.keys[:i] + [pivot] + parent.keys[i:]
                parent.values = parent.values[:i] + child.values + parent.values[i:]
                break

            elif i + 1 == len(parent.keys):
                parent.keys += [pivot]
                parent.values += child.values
                break

    def insert(self, key, value):

        parent = None
        child = self.root

        while not child.leaf:
            parent = child
            child, index = self._find(child, key)

        child.add(key, value)

        if child.is_full():
            child.split()

            if parent and not parent.is_full():
                self._balance(parent, child, index)

    def search(self, key):
 
        child = self.root

        while not child.leaf:
            child, index = self._find(child, key)

        print("-----------------------")

        for i, item in enumerate(child.keys):
            print("Pedido ", i , " -> ", child.values[i])
            if key == item:
                return child.values[i]
        
        print("-----------------------")
        print("👇  Recomendado 👇")
        print("🌎  Posicion: ")
        print("\t\tLongitud:", key.split("$",1)[0])
        print("\t\tLatitud:", key.split("$",1)[1])
        print("\t\tType:  🚀 URGENTE ")
        return child.values[0]
        # return None

    def show(self):
        self.root.show()
