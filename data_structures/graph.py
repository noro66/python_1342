from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for other_vrtx in self.adj_list[vertex]:
                self.adj_list[other_vrtx].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

    def bfs(self):
        visited = set()
        queue = deque()
        source = 1
        visited.add(source)
        queue.append(source)
        while queue:
            print(queue, visited)
            u = queue.popleft()

            for i in range(1, len(self.adj_list)):
                if i in self.adj_list[u] and i not in visited:
                    visited.add(i)
                    queue.append(i)


def main():
    graph = Graph()
    for i in range(6):
        graph.add_vertex(i + 1)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(3, 4)
    graph.add_edge(3, 5)
    graph.add_edge(4, 2)
    graph.add_edge(5, 4)

    # graph.print_graph()
    graph.bfs()


if __name__ == "__main__":
    main()
