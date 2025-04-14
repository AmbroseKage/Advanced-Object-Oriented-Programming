from typing import List, NamedTuple, Tuple
import networkx as nx

VertexID = int
EdgeID = int

class TrailSegmentEntry(NamedTuple):
    vertex_begin_id: VertexID
    vertex_end_id: VertexID
    edge_id: EdgeID
    weight: float

Trail = List[TrailSegmentEntry]

def load_multigraph_from_file(filepath: str) -> nx.MultiDiGraph:
    edges: List[Tuple[int, int, float]] = []
    with open(filepath) as f:
        for line in f:
            if line.strip():
                tokens = line.split()
                edges.append((int(tokens[0]), int(tokens[1]), float(tokens[2])))
                
    g = nx.MultiDiGraph()
    g.add_weighted_edges_from(edges)
    return g

def find_min_trail(g: nx.MultiDiGraph, v_start: VertexID, v_end: VertexID) -> Trail:
    dijkstra_path_nodes = nx.dijkstra_path(g, v_start, v_end)
    edges_in_path = list(zip(dijkstra_path_nodes[:-1], dijkstra_path_nodes[1:]))
    
    trail: Trail = []
    for u, v in edges_in_path:
        min_edge_id = min(g[u][v], key=lambda k: g[u][v][k]['weight'])
        trail.append(TrailSegmentEntry(
            vertex_begin_id=u,
            vertex_end_id=v,
            edge_id=min_edge_id,
            weight=g[u][v][min_edge_id]['weight']
        ))
    return trail

def trail_to_str(trail: Trail) -> str:
    output = ''
    total_weight = sum(segment.weight for segment in trail)
    for segment in trail:
        output += f'{segment.vertex_begin_id} -[{segment.edge_id}: {segment.weight}]-> '
    output += f'{trail[-1].vertex_end_id}  (total = {total_weight})'
    return output
