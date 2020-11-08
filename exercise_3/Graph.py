from math import inf
from typing import List, Mapping


class Node:

    def __init__(self, i, out_edges: List):
        self._capacity = out_edges
        self._flow = [0 for _ in self._capacity]
        self._index = i

    def capacity(self, node: "Node"):
        return self._capacity[node._index]

    def flow(self, node: "Node"):
        return self._flow[node._index]

    def set_flow(self, node: "Node", flow: int):
        if flow > self._capacity[node._index]:
            raise ValueError("Flow higher than allowed")
        self._flow[node._index] = flow

    def is_source(self):
        return self._index == 0

    def is_sink(self):
        return self._index == len(self._capacity) - 1

    def residual(self, node: "Node"):
        return self._capacity[node._index] - self._flow[node._index]

    def maxed(self, ):
        return all(self._flow[i] == self._capacity[i] for i in range(len(self._capacity)) if self._capacity[i] > 0 )

    def _validate(self):
        if self._capacity[0] != 0:
            raise ValueError(f"Node capacity edges={self._capacity} edge to source is not 0")
        if self.is_sink() and sum(self._capacity) != 0:
            raise ValueError(f"Sink Node edges={self._capacity[-1]} contains edge with capacity not 0")

    def edges(self, graph) -> List["Node"]:
        return [node for i, node in enumerate(graph) if self._capacity[i] > 0]

    def __str__(self):
        return f"Node(i={self._index}, cap={self._capacity}, flow={self._flow}"


class Graph:
    """Understands capacity flow in a directed graph"""

    def __init__(self, config):
        self._nodes: List[Node] = self._create_nodes(config)
        self._source = self._nodes[0]
        self._sink = self._nodes[-1]
        self._bfs_runs = 0
        self._computed = False
        self._max_flow = None

    def _create_nodes(self, config) -> List[Node]:
        self._validate(config)
        return [Node(i, out_edges) for i, out_edges in enumerate(config)]

    def __len__(self):
        return len(self._nodes)

    def _validate(self, config):
        for node_edges in config:
            if len(node_edges) != len(config):
                raise ValueError(f"number of edges={len(node_edges)} is not equal to number of nodes={len(config)}")

    def max_flow(self):
        if not self._computed:
            self._ford_fulkerson()
        return self._max_flow

    def steps(self):
        if not self._computed:
            self._ford_fulkerson()
        return self._bfs_runs

    def flow_graph(self):
        if not self._computed:
            self._ford_fulkerson()
        return [[node.flow(node_i) for node_i in self._nodes] for node in self._nodes]

    def maxed(self):
        if not self._computed:
            self._ford_fulkerson()
        maxed_cut = [self._source]
        queue = []
        cur = self._source
        while cur != self._sink:
            for node in cur.edges(self._nodes):
                if node != self._sink and node.maxed():
                    maxed_cut.append(node)
                    queue.append(node)
            if not queue:
                break
            cur = queue.pop()
        return sorted([node._index for node in maxed_cut])

    def _ford_fulkerson(self):
        max_flow = 0
        while augmenting_path := self._bfs():
            if augmenting_path[self._sink] is None:
                break  # No more augmenting paths
            path_flow = inf
            cur = self._sink
            while cur != self._source:
                path_flow = min(path_flow, augmenting_path[cur].residual(cur))
                cur = augmenting_path[cur]

            max_flow += path_flow

            cur = self._sink
            while cur != self._source:
                u = augmenting_path[cur]
                u.set_flow(cur, u.flow(cur) + path_flow)
                cur = augmenting_path[cur]

        self._computed = True
        self._max_flow = max_flow

    def _bfs(self) -> Mapping:
        self._bfs_runs += 1
        parent = {node: None for node in self._nodes}
        visited = {node: False for node in self._nodes}
        queue: List[Node] = [self._source]

        while queue:
            cur = queue.pop()

            for node in cur.edges(self._nodes):
                if not visited[node] and cur.residual(node):
                    queue.append(node)
                    visited[node] = True
                    parent[node] = cur
        return parent


def has_edge_to(graph: List[Node], node: Node) -> List[Node]:
    has_edge = []
    for inode in graph:
        if node in inode.edges(graph):
            has_edge.append(inode)
    return has_edge

