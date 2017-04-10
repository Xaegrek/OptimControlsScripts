import Node, time


class Djikstra(object):
    def __init__(self, start_id):
        self.start_id = start_id
        self.toVisit = [Node.Node(start_id, None, 0)]

    def run(self):
        while not self.toVisit[0].complete():
            nodes = self.toVisit.pop(0).expand()

            for n in nodes:
                if not self.toVisit:
                    self.toVisit.append(n)
                else:
                    for idx, v in enumerate(self.toVisit):
                        if (n.cost < v.cost):
                            self.toVisit.insert(idx, n)
                            break
                        elif (idx is len(self.toVisit) - 1):
                            self.toVisit.append(n)
                            break

        goal = self.toVisit[0]
        print(goal.lineage())
