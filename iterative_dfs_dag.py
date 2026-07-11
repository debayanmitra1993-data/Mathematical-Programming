graph = {}
for node in range(V):
  graph[node] = []
for edge in edges:
  src, dest = edge[0], edge[1]
  graph[src].append(dest)

visited = set()

while len(visited) < V:
  for node in range(V):
    if node not in visited:
      break
  
  dfsstack = []
  dfsstack.append(node)

  while len(dfsstack) > 0:
    popped_node = dfsstack.pop()
    if popped_node not in visited:
      visited.add(popped_node)
    else:
      continue
    for childnode in graph[popped_node]:
      if childnode not in visited:
        dfsstack.append(childnode)

print("visited = ", visited)
