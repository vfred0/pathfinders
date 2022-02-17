import pygraphviz as pgv
from Node import Node


class Draw:
    def __init__(
        self,
        nodes: list[Node],
        show_weight: bool = True,
        file_name: str = "graph",
    ) -> None:
        self.__name = f"{file_name}.jpg"
        self.__nodes = nodes
        self.__graph = None
        self.__show_weight = show_weight

    def show_path_graph(self, directed: bool, nodes: list[Node]):
        self.__set_graph(directed)
        for node in nodes:
            print("rutita")
            node = self.__graph.get_node(node)
            node.attr["style"] = "filled"
            node.attr["color"] = "#40e0d0"
            node.attr["fontcolor"] = "white"

        for index, node in enumerate(nodes[:-1]):
            self.__graph.add_edge(node, nodes[index + 1], color="#40e0d0", penwidth="3")
        self.__name = f"{self.__name}-path.jpg"
        self.__draw()

    def __draw(self) -> None:
        # neato, dot, twopi, circo, fdp, nop, gc, acyclic, gvpr, gvcolor, ccomps, sccmap, tred, sfdp, unflatten
        self.__graph.draw(self.__name, prog="dot")

    def show_graph(self, directed: bool):
        self.__set_graph(directed)
        self.__draw()

    def __set_graph(self, directed: bool):  # cambiar esto
        self.__graph = pgv.AGraph(directed=directed)
        for parent in self.__nodes:
            self.__graph.add_node(parent)
        edge = 1
        for parent in self.__nodes:
            for children, weight in parent.get_childrens():
                label = (
                    f"[A{edge}, {str(weight)}]" if self.__show_weight else f"A{edge}"
                )
                self.__graph.add_edge(parent, children, label=label)
                edge += 1


# for i, x in enumerate([1, 2, 4, 5]):
#     print(i, x)
