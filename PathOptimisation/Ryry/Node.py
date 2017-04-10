import numpy as np

dist = np.matrix([[0, 51, 217, 169, 454],
                  [51, 0, 182, 163, 449],
                  [217, 182, 0, 151, 373],
                  [169, 163, 151, 0, 289],
                  [454, 449, 373, 289, 0]])


class Node(object):
    def __init__(self, id, parent, cost):
        self.id = id
        self.parent = parent
        self.cost = cost

    def expand(self):
        toReturn = []

        for i in range(0, 5):
            node = Node(i, self, self.cost + dist[self.id, i])
            if self.contains(i):
                pass
            else:
                toReturn.append(node)

        return toReturn

    def contains(self, id):
        if self.id is id:
            return True
        elif not self.parent:
            return False
        else:
            return self.parent.contains(id)

    def complete(self):
        for i in range(0, 5):
            if not self.contains(i):
                return False
        return True

    def lineage(self):
        if not self.parent:
            return [self.id, self.cost]
        else:
            return [self.id, self.cost, self.parent.lineage()]
