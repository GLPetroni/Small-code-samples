# Course: CS261 - Data Structures
# Author:
# Assignment:
# Description:

class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        TODO: Write this implementation
        """
        self.v_count += 1
        for j in range(self.v_count-1):
            self.adj_matrix[j].append(0)
        self.adj_matrix.append([0]*self.v_count)
        return self.v_count

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        TODO: Write this implementation
        """
        if 0 > src or src >= len(self.adj_matrix):
            return
        if 0 > dst or dst >= len(self.adj_matrix):
            return
        if src == dst or weight <= 0:
            return
        self.adj_matrix[src][dst] = weight

    def remove_edge(self, src: int, dst: int) -> None:
        """
        TODO: Write this implementation
        """
        if src < 0 or src >= len(self.adj_matrix):
            return
        if dst < 0 or dst >= len(self.adj_matrix):
            return
        if src == dst:
            return
        self.adj_matrix[src][dst] = 0

    def get_vertices(self) -> []:
        """
        TODO: Write this implementation
        """
        visited = []
        if len(self.adj_matrix) == 0:
            return visited
        visited.append(0)
        for i, neighbor in enumerate(self.adj_matrix):
                if i > 0 and i not in visited:
                    visited.append(i)
        return visited

    def get_edges(self) -> []:
        """
        TODO: Write this implementation
        """
        visited = []
        if len(self.adj_matrix) == 0:
            return visited
        for i, neighbor in enumerate(self.adj_matrix):
            for j, k in enumerate(neighbor):
                if k:
                    visited.append((i,j,k))
        return visited

    def is_valid_path(self, path: []) -> bool:
        """
        TODO: Write this implementation
        """
        vistied = []
        if not path:
            return True
        for i in range(1,len(path)):
            k = path[i-1]
            l = path[i]
            if k < 0 or k >= len(self.adj_matrix):
                return False
            if i < 0 or i >= len(self.adj_matrix):
                return False
            if self.adj_matrix[k][l] == 0:
                return False
        return True
        #    for j in self.adj_matrix[k]:
        #        if j > 0 and i not in vistied:
        #            return True
        #        vistied.append(i)
        #    tmp.append(k)
        #path = tmp
        #return False

    def dfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
        if v_start < 0 or v_start > len(self.adj_matrix):
            return []
        visited = []
        s = [v_start]
        while len(s) > 0:
            x = s.pop()
            if x == v_end:
                return visited
            if x not in visited:
                visited.append(x)
            tmp = self.adj_matrix[x]
            for j in range(len(self.adj_matrix)-1,-1,-1):
                if tmp[j] != 0:
                    if j not in visited:
                        s.append(j)
        return visited


    def bfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
        if v_start < 0 or v_start > len(self.adj_matrix):
            return []
        visited = []
        s = [v_start]
        while len(s) > 0:
            x = s.pop(0)
            if x == v_end:
                visited.append(x)
                return visited
            if x not in visited:
                visited.append(x)
            tmp = self.adj_matrix[x]
            for j in range(len(self.adj_matrix)):
                if tmp[j] != 0 and j not in visited:
                    s.append(j)
                    visited.append(j)
        return visited

    def has_cycle(self):
        """
        TODO: Write this implementation
        """
        visited = {}
        for neighbor in range(len(self.adj_matrix)-1):
            if neighbor not in visited:
                if self.cycle_help(neighbor, visited, -1) == True:
                    return True
        return False
    def cycle_help(self,neighbor,visited, parent):
        visited[neighbor]=0
        for i in self.adj_matrix[neighbor]:
            if i not in visited:
                self.cycle_help(parent,visited,i)
            elif i != parent and visited[i] == 0:
                return True
        visited[neighbor] = 1
        return False


    def dijkstra(self, src: int) -> []:
        """
        TODO: Write this implementation
        """
        pass


if __name__ == '__main__':

    #print("\nPDF - method add_vertex() / add_edge example 1")
    #print("----------------------------------------------")
    #g = DirectedGraph()
    #print(g)
    #for _ in range(5):
    #    g.add_vertex()
    #print(g)

    #edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #         (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    #for src, dst, weight in edges:
    #    g.add_edge(src, dst, weight)
    #print(g)


    #print("\nPDF - method get_edges() example 1")
    #print("----------------------------------")
    #g = DirectedGraph()
    #print(g.get_edges(), g.get_vertices(), sep='\n')
    #edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #         (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    #g = DirectedGraph(edges)
    #print(g.get_edges(), g.get_vertices(), sep='\n')


    #print("\nPDF - method is_valid_path() example 1")
    #print("--------------------------------------")
    #edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #         (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    #g = DirectedGraph(edges)
    #test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    #for path in test_cases:
    #    print(path, g.is_valid_path(path))


    #print("\nPDF - method dfs() and bfs() example 1")
    #print("--------------------------------------")
    #edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #         (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    #g = DirectedGraph(edges)
    #for start in range(5):
    #    print(f'{start} BFS:{g.bfs(start)} DFS:{g.dfs(start)}')


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)

    edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    for src, dst in edges_to_remove:
        g.remove_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')

    edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    for src, dst in edges_to_add:
        g.add_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')
    print('\n', g)


    #print("\nPDF - dijkstra() example 1")
    #print("--------------------------")
    #edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #         (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    #g = DirectedGraph(edges)
    #for i in range(5):
    #    print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    #g.remove_edge(4, 3)
    #print('\n', g)
    #for i in range(5):
    #    print(f'DIJKSTRA {i} {g.dijkstra(i)}')
