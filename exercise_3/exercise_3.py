from typing import List

from exercise_3.Graph import Graph


class Exercise3:

    def __init__(self, problem_text):
        self._n = self._parse_n(problem_text)
        self._graph_edges = self._parse_graph(problem_text)

    def _parse_n(self, problem_text) -> int:
        return int(problem_text.split()[0])

    def _parse_graph(self, problem_text) -> List:
        graph_config = []
        problem_edges = problem_text.split()[1:]  # remove n from input
        i = self._n
        while i - self._n < len(problem_edges) :
            row = problem_edges[i - self._n: i]
            graph_config.append([int(edge) for edge in row])
            i += self._n
        return graph_config

    def solution(self):
        g = Graph(self._graph_edges)

        return f"Max Flow: {g.max_flow()}\n" +\
               f"Cut: {' '.join(str(node) for node in g.min_cut())}\n" +\
               f"Steps: {g.steps()}\n" + \
               self._rapport_graph(g.flow_graph()).lstrip()

    def _rapport_graph(self, flow_graph) -> str:
        graph_str = ""
        for node in flow_graph:
            graph_str += " ".join(str(edge) for edge in node) + "\n"
        return graph_str
