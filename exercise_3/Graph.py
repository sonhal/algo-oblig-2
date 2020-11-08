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

    def _validate(self):
        if self._capacity[0] != 0:
            raise ValueError(f"Node capacity edges={self._capacity} edge to source is not 0")
        if self.is_sink() and sum(self._capacity) != 0:
            raise ValueError(f"Sink Node edges={self._capacity[-1]} contains edge with capacity not 0")

    def edges(self, graph) -> List["Node"]:
        return [node for i, node in enumerate(graph) if self._capacity[i] > 0]


class Graph:
    """Understands capacity flow in a directed graph"""

    def __init__(self, config):
        self._nodes: List[Node] = self._create_nodes(config)
        self._source = self._nodes[0]
        self._sink = self._nodes[-1]

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
        return self._ford_fulkerson()

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

        return max_flow

    def _bfs(self) -> Mapping:
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







