from typing import List, Set, Dict
from collections import deque

VertexID = int
AdjList = Dict[VertexID, List[VertexID]]
Distance = int

def neighbors(adjlist: AdjList, start_vertex_id: VertexID, max_distance: Distance) -> Set[VertexID]:
    visited = {start_vertex_id}
    queue = deque([(start_vertex_id, 0)])
    result = set()

    while queue:
        current, distance = queue.popleft()
        if distance >= max_distance:
            continue
        
        for neighbor in adjlist.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                result.add(neighbor)
                queue.append((neighbor, distance + 1))
                
    return result

def quicksort(in_array: List[int]) -> List[int]:
    if len(in_array) <= 1:
        return in_array
    
    stack = [(0, len(in_array) - 1)]
    result = in_array[:]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(result, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))
    
    return result

def partition(array: List[int], low: int, high: int) -> int:
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1
