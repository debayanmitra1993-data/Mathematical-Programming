class Solution:
    def isCyclic(self, V, edges):
        # code here
        graph = {}
        for node in range(V):
            graph[node] = []
        for edge in edges:
            src, dest = edge[0], edge[1]
            graph[src].append(dest)
        
        visited = set()
        cyclecheck = [False]
        while len(visited) < V:
            for srcnode in range(V):
                if srcnode not in visited:
                    break 
            path = set()
            self.dfscyclecheck(graph, srcnode, visited, path, cyclecheck)
            if cyclecheck[0] == True:
                return True 
        return cyclecheck[0]
    
    def dfscyclecheck(self, graph, node, visited, path, cyclecheck):
        if cyclecheck[0] == True:
            return 
    
        visited.add(node)
        path.add(node)
        
        for childnode in graph[node]:
            if childnode not in visited:
                self.dfscyclecheck(graph, childnode, visited, path, cyclecheck)
            elif childnode in visited:
                if childnode not in path:
                    pass
                elif childnode in path:
                    cyclecheck[0] = True 
                    return 
        path.remove(node)
