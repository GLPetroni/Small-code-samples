# Course: 
# Author: 
# Assignment: 
# Description:


class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        Add new vertex to the graph
        """
        self.adj_list[v] = []

    def add_edge(self, u: str, v: str) -> None:
        """
        Add edge to the graph
        """
        if u == v:
            return
        if u not in self.adj_list:
            self.add_vertex(u)
        if v not in self.adj_list:
            self.add_vertex(v)
        if v in self.adj_list[u]:
            return
        if self.adj_list[u] == v or self.adj_list[v] == u:
            return
        for i in self.adj_list.keys():
            if i == u:
                self.adj_list[u].append(v)
                self.adj_list[v].append(u)


    def remove_edge(self, v: str, u: str) -> None:
        """
        Remove edge from the graph
        """

        if u == v:
            return
        if u not in self.adj_list or v not in self.adj_list:
            return
        if self.adj_list[u] == v or self.adj_list[v] == u:
            return
        if v in self.adj_list[u]:
            self.adj_list[u].remove(v)
        if u in self.adj_list[v]:
            self.adj_list[v].remove(u)

    def remove_vertex(self, v: str) -> None:
        """
        Remove vertex and all connected edges
        """
        if v not in self.adj_list:
            return
        for i in self.adj_list:
            if i == v:
                for j in self.adj_list:
                    self.remove_edge(v,j)
        self.adj_list.pop(v)

    def get_vertices(self) -> []:
        """
        Return list of vertices in the graph (any order)
        """
        vert = []
        if len(self.adj_list)==0:
            return vert
        for i in self.adj_list.keys():
            vert.append(i)
        return vert
       

    def get_edges(self) -> []:
        """
        Return list of edges in the graph (any order)
        """
        edg = []
        tmp = []
        tmp2 = []
        if len(self.adj_list)==0:
            return edg
        for key in self.adj_list:
            for value in self.adj_list[key]:
                if key != value:
                    tmp = (key,value)
                    tmp2 = (value,key)
                    if (tmp and tmp2) not in edg:
                        edg.append(tmp)
        return edg

    def is_valid_path(self, path: []) -> bool:
        """
        Return true if provided path is valid, False otherwise
        """
        if not path:
            return True
        if path[0] not in self.adj_list:
            return False
        for x in path[1:]:
            k = path.pop(0)
            if x not in self.adj_list[k]:
                return False
        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during DFS searchV
        Vertices are picked in alphabetical orderV
        """
        if v_start not in self.adj_list:
            return []
        visit = []
        s = []
        s.append(v_start)
        while len(s)>0:
            x = s.pop()
            if x == v_end:
                visit.append(x)
                return visit
            if x not in visit:
                visit.append(x)
            tmp = sorted(self.adj_list[x], reverse=True)
            for j in tmp:
                if j not in visit:
                    s.append(j)
        return visit

    def bfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during BFS search
        Vertices are picked in alphabetical order
        """
        if v_start not in self.adj_list:
            return []
        visit = []
        s = []
        s.append(v_start)
        while len(s)>0:
            x = s.pop(0)
            if x == v_end:
                visit.append(x)
                return visit
            if x not in visit:
                visit.append(x)
            tmp = sorted(self.adj_list[x])
            for j in tmp:
                if j not in visit:
                    s.append(j)

        return visit


    def count_connected_components(self):
        """
        Return number of connected componets in the graph
        """
        visit = []
        count = 0
        for i in self.adj_list.keys():
            if i not in visit:
                count+=1
                for x in self.dfs(i):
                    visit.append(x)
        return count


    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise
        """
        visit = {}
        for i in self.adj_list:
            if self.has_cycle_help(i,-1,visit)== True:
                return True
        return False
    def has_cycle_help(self,i,parent,visit):
        visit[i] =0
        for p in self.adj_list[i]:
            if p not in visit:
                self.has_cycle_help(p,i,visit)
            elif p != parent and visit[p] == 0:
                return True
        visit[i] = 1
        return False


if __name__ == '__main__':

    #print("\nPDF - method add_vertex() / add_edge example 1")
    #print("----------------------------------------------")
    #g = UndirectedGraph()
    #print(g)

    #for v in 'ABCDE':
    #   g.add_vertex(v)
    #print(g)

    #g.add_vertex('A')
    #print(g)

    #for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
    #    g.add_edge(u, v)
    #print(g)


    #print("\nPDF - method remove_edge() / remove_vertex example 1")
    #print("----------------------------------------------------")
    #g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    ##g.remove_vertex('DOES NOT EXIST')
    #g.remove_edge('A', 'B')
    #g.remove_edge('X', 'B')
    #print(g)
    #g.remove_vertex('D')
    #print(g)


    #print("\nPDF - method get_vertices() / get_edges() example 1")
    #print("---------------------------------------------------")
    #g = UndirectedGraph()
    #print(g.get_edges(), g.get_vertices(), sep='\n')
    #g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    #print(g.get_edges(), g.get_vertices(), sep='\n')


    #print("\nPDF - method is_valid_path() example 1")
    #print("--------------------------------------")
    #g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    #test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    #for path in test_cases:
    #    print(list(path), g.is_valid_path(list(path)))


    #print("\nPDF - method dfs() and bfs() example 1")
    #print("--------------------------------------")
    #edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    #g = UndirectedGraph(edges)
    #test_cases = 'ABCDEGH'
    #for case in test_cases:
    #    print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    #print('-----')
    #for i in range(1, len(test_cases)):
    #    v1, v2 = test_cases[i], test_cases[-1 - i]
    #    print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')


    #print("\nPDF - method count_connected_components() example 1")
    #print("---------------------------------------------------")
    #edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    #g = UndirectedGraph(edges)
    #test_cases = (
    #    'add QH', 'remove FG', 'remove GQ', 'remove HQ',
    #    'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
    #    'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
    #    'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    #for case in test_cases:
    #    command, edge = case.split()
    #    u, v = edge
    #    g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
    #    print(g.count_connected_components(), end=' ')
    #print()


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
        'add FG', 'remove GE')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print('{:<10}'.format(case), g.has_cycle())
