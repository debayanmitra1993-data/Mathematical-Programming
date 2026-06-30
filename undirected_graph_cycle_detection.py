class Solution:
	def isCycle(self, V, edges):
		#Code here
		graph = {}
		for node in range(V):
		    graph[node] = []
		for edge in edges:
		    src, dest = edge[0], edge[1]
		    graph[src].append(dest)
		    graph[dest].append(src)
		
		visited = set()
		cyclecheck = [False]
		while len(visited) < V:
		    for startnode in range(V):
		        if startnode not in visited:
		            break

		    self.dfscyclecheck(graph, visited, startnode, None, cyclecheck)
		    
		    if cyclecheck[0] == True:
		        return True
		return cyclecheck[0]
	
	def dfscyclecheck(self, graph, visited, node, parentnode, cyclecheck):
	    if cyclecheck[0] == True:
	        return 

	    visited.add(node)
	    
	    for childnode in graph[node]:
	        if childnode in visited:
	            if childnode != parentnode:
	                cyclecheck[0] = True
	                return 
	        elif childnode not in visited:
	            self.dfscyclecheck(graph, visited, childnode, node, cyclecheck)
	        
	    
	    
