class DirectedGraph():
    def __init__(self):
        self.nodes = {}

    def add_edge(self, node_a, node_b):
        if node_a in self.nodes:
            self.nodes[node_a].append(node_b)
        else:
            self.nodes[node_a] = [node_b, ]

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = []

    def get_neighbours_for(self, node):
        if node not in self.nodes:
            return None
        else:
            return self.nodes[node]

    def path_between(self, node_a, node_b):
            visited = set()
            queue = []
            path_to = {}

            visited.add(node_a)
            queue.append(node_a)
            path_to[node_a] = None
            found = False
            path_length = 0

            while len(queue) != 0:
                current_node = queue.pop(0)
                if current_node == node_b:
                    found = True
                    break

                if current_node in self.nodes:
                    for neighbour in self.nodes[current_node]:
                        if neighbour not in visited:
                            path_to[neighbour] = current_node
                            visited.add(neighbour)
                            queue.append(neighbour)

            if found:
                while path_to[node_b] is not None:
                    path_length += 1
                    node_b = path_to[node_b]

            if path_length == 0:
                return False
            else:
                return True

    def edge_between(self, node_a, node_b):
        if len(self.get_neighbours_for(node_a, node_b)) > 0:
            return True
        else:
            return False
