from collections import deque

mumbai_map = {
    'Chakala': ['WEH Metro', 'Andheri Kurla Road', 'JB Nagar', 'Holy Family Church'],
    
    # Route 1 (Via WEH Metro)
    'WEH Metro': ['Gundavali'],
    
    # Route 2 (Via Main Road)
    'Andheri Kurla Road': ['Gundavali'],
    
    # Route 3 (Via JB Nagar Internal)
    'JB Nagar': ['Tarun Bharat Society'],
    'Tarun Bharat Society': ['Pump House'],
    
    # Route 4 (Via Holy Family Church)
    'Holy Family Church': ['Pump House'],
    
    # Converging Nodes
    'Gundavali': ['MVLU College'],
    'Pump House': ['MVLU College'],
    
    # Destination
    'MVLU College': []
}

# A) Breadth First Search (BFS) Implementation
def bfs_shortest_path(graph, start, destination):
    queue = deque([(start, [start])])
    visited = set([start])
    nodes_explored_count = 0
    
    while queue:
        current, path = queue.popleft()
        nodes_explored_count += 1
        
        if current == destination:
            return path, nodes_explored_count
            
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                
    return None, nodes_explored_count

# B) Iterative Depth First Search (DFS) Implementation
def iterative_dfs_path(graph, start, destination):
    stack = [(start, [start])]
    visited = set()
    nodes_explored_count = 0
    
    while stack:
        current, path = stack.pop()
        nodes_explored_count += 1
        
        if current == destination:
            return path, nodes_explored_count
            
        if current not in visited:
            visited.add(current)
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
                    
    return None, nodes_explored_count

# Execution
start_node = 'Chakala'
end_node = 'MVLU College'

bfs_path, bfs_count = bfs_shortest_path(mumbai_map, start_node, end_node)
dfs_path, dfs_count = iterative_dfs_path(mumbai_map, start_node, end_node)

print("--- BFS Results ---")
print(f"Path Found: {' -> '.join(bfs_path)}")
print(f"Total Steps (Edges): {len(bfs_path) - 1}")
print(f"Total Nodes Visited/Checked: {bfs_count}\n")

print("--- Iterative DFS Results ---")
print(f"Path Found: {' -> '.join(dfs_path)}")
print(f"Total Steps (Edges): {len(dfs_path) - 1}")
print(f"Total Nodes Visited/Checked: {dfs_count}")
