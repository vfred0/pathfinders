from InformedSearch import InformedSearch
from Vertex import Vertex


class Dijkstra(InformedSearch):
    def __init__(self, start: Vertex, goal: Vertex) -> None:
        super().__init__(start, goal)

    def _search_condition(self, children_of_vertexs_visited: list[Vertex]) -> bool:

        return children_of_vertexs_visited

    def shortest_path(self):
        super().shortest_path()
        super()._show_path()
