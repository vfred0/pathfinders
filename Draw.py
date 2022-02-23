import pygraphviz as pgv
from Vertex import Vertex


class Draw:
    def __init__(
        self,
        vertexs: list[Vertex],
        file_name: str = "graph",
    ) -> None:
        self.__file_name = f"{file_name}"
        self.__vertexs = vertexs
        self.__graph = None

    def show_path_graph(self, vertexs: list[Vertex], color: str = "#40e0d0"):
        self.__set_graph()
        self.__graph.add_nodes_from(vertexs, style="filled", color=color)
        position = 0
        for vertex in vertexs[position:]:
            position = vertexs.index(vertex)
            for next_vertex in vertexs[position : position + 2]:
                if vertex != next_vertex:
                    number_edge = self.__get_number_edge(vertex, next_vertex)
                    self.__add_edge(
                        vertex,
                        next_vertex,
                        f"[{number_edge}, {next_vertex.get_cost()}]",
                        color,
                    )

        if not self.__file_name.__contains__("-path"):
            self.__file_name = f"{self.__file_name}-path"
        self.__draw()

    def __add_edge(
        self, vertexA: Vertex, vertexB: Vertex, label: str, color: str
    ) -> None:
        if self.__graph.has_edge(vertexA, vertexB):
            self.__graph.remove_edge(vertexA, vertexB)
        self.__graph.add_edge(
            vertexA,
            vertexB,
            color=color,
            penwidth="3",
            fontcolor=color,
            label=label,
        )

    def __get_number_edge(self, vertexA: Vertex, vertexB: Vertex) -> str:

        # try:
        #     edge = self.__graph.get_edge(vertexA, vertexB)
        # except KeyError:
        #     return None

        edge = self.__graph.get_edge(vertexA, vertexB)
        if edge:
            return str(edge.attr["label"].split(",")[0]).replace("[", "")
        return None

    def __draw(self) -> None:
        # neato, dot, twopi, circo, fdp, nop, gc, acyclic, gvpr, gvcolor, ccomps, sccmap, tred, sfdp, unflatten
        self.__graph.draw(f"{self.__file_name}.png", prog="dot")

    def show_graph(self):
        self.__set_graph()
        self.__draw()

    def set_file_name(self, file_name: str = "graph") -> None:
        self.__file_name = f"{file_name}"

    def __set_graph(self):
        self.__graph = pgv.AGraph(ranksep="0.1", strict=False, directed=True)
        self.__graph.add_nodes_from(self.__vertexs)
        edge = 0
        for parent in self.__vertexs:
            for children, cost in parent.get_childrens():
                self.__graph.add_edge(
                    parent, children, label=self.__get_label(edge + 1, cost)
                )
                edge += 1

    def __get_label(self, edge: int, cost: int) -> str:
        return f"[A{edge}, {cost}]"


# l = [1, 2, 3, 4, 5, 6, 7]
# p = 0
# for i in l[p:]:
# for j in l[p : p + 2]:
#     p += 1
#     print(p)


# print(l[:2])
# print(l[1:3])
# print(l[2:4])
