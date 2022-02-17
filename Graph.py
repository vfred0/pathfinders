from Dijkstra import Dijkstra
from InformedSearch import InformedSearch
from Node import Node
from Draw import Draw
from TypesInformedSearch import TypesInformedSearch
from UniformCost import UniformCost


class Graph:
    def __init__(
        self,
        matrix_adjancency: list[int] = [],
        nodes: list[Node] = [],
        file_name: str = "graph",
        show_weight: bool = True,
    ) -> None:
        self.__nodes = nodes
        self.__matrix_adjancency = matrix_adjancency
        self.__set_nodes_or_adjancency_matrix()
        self.__draw = Draw(self.__nodes, show_weight, file_name)

    def __is_directed_adjancency_matrix(self) -> bool:
        for node in self.__nodes:
            for next_node in self.__nodes[self.__get_position(node) :]:
                if node != next_node and next_node.contains(node):
                    return False
        return True

    def __set_nodes_or_adjancency_matrix(self) -> None:

        if len(self.__matrix_adjancency) == 0:
            lenght = len(self.__nodes)
            for i in range(lenght):
                self.__matrix_adjancency.append([0] * lenght)
            for parent in self.__nodes:
                for children, weight in parent.get_childrens():
                    self.__set_weight(
                        self.__get_position(parent),
                        self.__get_position(children),
                        weight,
                    )
        else:
            for i in range(len(self.__matrix_adjancency)):
                self.__nodes.append(Node(f"Node{i+1}"))

            for parent_position, childrens_positions in enumerate(
                self.__matrix_adjancency
            ):
                childrens = {}
                for children_position, weight in enumerate(childrens_positions):
                    if weight > 0:
                        childrens.update({self.__get_node(children_position): weight})
                self.__get_node(parent_position).add(childrens)

    def __get_node(self, node_position: int) -> Node:
        return self.__nodes[node_position]

    def __set_weight(self, parent: int, children: int, weight: int) -> None:
        self.__matrix_adjancency[parent][children] = weight
        self.__matrix_adjancency[children][parent] = weight

    def get_matrix_adjancency(self) -> list:
        return self.__matrix_adjancency

    def get_matrix_adjancency(self) -> list:
        return self.__matrix_adjancency

    def __get_position(self, search_node: Node) -> int:
        for index, node in enumerate(self.__nodes):
            if node == search_node:
                return index
        return 0

    def show(self) -> None:
        self.__draw.show_graph(self.__is_directed_adjancency_matrix())

    def shortest_path(
        self, types_informed_search: TypesInformedSearch, start: Node, goal: Node
    ):
        informed_search: InformedSearch = None
        if types_informed_search.is_dijkstra():
            informed_search = Dijkstra(start, goal)
        else:
            informed_search = UniformCost(start, goal)

        informed_search.shortest_path()

        self.__draw.show_path_graph(directed=True, nodes=informed_search.get_route())

    def find_shortest_path_with_positions(
        self, start_node_position: int, end_node_position
    ):
        return self.shortest_path(
            self.__get_node(start_node_position - 1),
            self.__get_node(end_node_position - 1),
        )


nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")


nodeA.add({nodeB: 168.5, nodeF: 144.63, nodeC: 318.71})
nodeB.add({nodeC: 198.16, nodeD: 246.56, nodeF: 193.84})
nodeC.add({nodeD: 142.34, nodeE: 140.04})
nodeD.add({nodeG: 137.18, nodeF: 155.46})
nodeE.add({nodeG: 289.11})


nodes = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG]
g = Graph(nodes=nodes, file_name="prueba")
g.show()

# print(g.get_matrix_adjancency())
g.shortest_path(TypesInformedSearch.UNIFORM_COST, nodeA, nodeG)

# g2 = Graph(matrix_adjancency=g.get_matrix_adjancency(), file_name="prueba2")
# g2.show()
# print(g2.get_matrix_adjancency())
# g2.shortest_path(TypesInformedSearch.UNIFORM_COST, nodeA, nodeG)

# UniformCost(nodeA, nodeG).shortest_path()
