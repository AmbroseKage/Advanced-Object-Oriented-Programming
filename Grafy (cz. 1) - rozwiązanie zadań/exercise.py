from typing import List, Dict

def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    adjlist = {}
    
    for i in range(len(adjmat)):
        neighbors = []
        for j in range(len(adjmat[i])):
            if adjmat[i][j] > 0:
                neighbors.extend([j + 1] * adjmat[i][j])
        if neighbors:  # Dodajemy tylko, jeśli są sąsiedzi
            adjlist[i + 1] = neighbors
    
    return adjlist

def dfs_recursive(G: Dict[int, List[int]], s: int, visited=None) -> List[int]:
    if visited is None:
        visited = []
    
    visited.append(s)
    
    for neighbor in G.get(s, []):  # Używamy G.get(s, []) zamiast G[s], by unikać błędów KeyError
        if neighbor not in visited:
            dfs_recursive(G, neighbor, visited)
    
    return visited

def dfs_iterative(G: Dict[int, List[int]], s: int) -> List[int]:
    stack = [s]
    visited = []
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            if vertex in G:
                stack.extend(reversed(G[vertex]))  # Sprawdzamy, czy vertex ma sąsiadów
    
    return visited

def is_acyclic(G: Dict[int, List[int]]) -> bool:
    visited = set()
    rec_stack = set()

    def dfs(v):
        visited.add(v)
        rec_stack.add(v)
        
        for neighbor in G.get(v, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        
        rec_stack.remove(v)
        return False

    for node in G:
        if node not in visited:
            if dfs(node):
                return False
    
    return True