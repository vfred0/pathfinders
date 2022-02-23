from Dijkstra import Dijkstra
from InformedSearch import InformedSearch
from Vertex import Vertex
from Draw import Draw
from TypesInformedSearch import TypesInformedSearch
from UniformCost import UniformCost


class Graph:
    def __init__(
        self, vertexs: list[Vertex] = [], adjancency_matrix: list[int] = []
    ) -> None:
        self.__vertexs = vertexs
        self.__adjancency_matrix = adjancency_matrix
        if not vertexs:
            self.__set_vertexs_from_adjancency_matrix()

        self.__draw = Draw(self.__vertexs)

    def __set_vertexs_from_adjancency_matrix(self) -> None:
        for i in range(len(self.__adjancency_matrix)):
            self.__vertexs.append(Vertex(f"Vértice{i+1}"))
        for parent_position, childrens_positions in enumerate(self.__adjancency_matrix):

            for children_position, cost in enumerate(childrens_positions):
                if cost > 0:
                    self.get_vertex(parent_position).add(
                        {self.get_vertex(children_position): cost}
                    )

    def get_vertex(self, position: int) -> Vertex:
        return self.__vertexs[position]

    def get_adjancency_matrix(self) -> list[int]:
        adjancency_matrix = []
        lenght = len(self.__vertexs)
        for i in range(lenght):
            adjancency_matrix.append([0] * lenght)
        for parent in self.__vertexs:
            for children, cost in parent.get_childrens():
                adjancency_matrix[self.__get_position(parent)][
                    self.__get_position(children)
                ] = cost
        return adjancency_matrix

    def show_adjancency_matrix(self) -> None:
        for i, row in enumerate(self.get_adjancency_matrix()):
            print(f"{self.get_vertex(i)}")
            for j, cost in enumerate(row):
                print(f"{self.get_vertex(j)}: {cost}")

        for i in self.get_adjancency_matrix():
            for j in i:
                print(f"{j} ", end="")
            print()

    def __get_position(self, search_vertex: Vertex) -> int:
        for index, vertex in enumerate(self.__vertexs):
            if vertex == search_vertex:
                return index
        return 0

    def get_vertexs(self) -> list[Vertex]:
        return self.__vertexs

    def show(self, file_name: str = "graph") -> None:
        self.__draw.set_file_name(file_name)
        self.__draw.show_graph()

    def show_shortest_path(
        self, types_informed_search: TypesInformedSearch, start: Vertex, goal: Vertex
    ):

        print(f"Realizar búsqueda desde {start} a {goal}")

        for i in self.__vertexs:
            i.reset()

        informed_search: InformedSearch = None
        if types_informed_search.is_dijkstra():
            informed_search = Dijkstra(start, goal)
        else:
            informed_search = UniformCost(start, goal)

        informed_search.shortest_path()
        if informed_search.exists_route():
            self.__draw.show_path_graph(informed_search.get_route())

    def shortest_path_with_positions(
        self,
        types_informed_search: TypesInformedSearch,
        start_vertex_position: int,
        goal_vertex_position: int,
    ):

        self.show_shortest_path(
            types_informed_search,
            self.get_vertex(start_vertex_position - 1),
            self.get_vertex(goal_vertex_position - 1),
        )


# a = Vertex("A")
# b = Vertex("B")
# c = Vertex("C")

# a.add({b: 2, c: 10})
# b.add({c: 2})

# graph = Graph([a, b, c])
# graph.show()
# graph.show_shortest_path(TypesInformedSearch.DIJKSTRA, c, b)
# graph.show_shortest_path(TypesInformedSearch.DIJKSTRA, c, b)
# graph.show_shortest_path(TypesInformedSearch.DIJKSTRA, c, b)
# graph.show_shortest_path(TypesInformedSearch.DIJKSTRA, c, b)
# graph.show_shortest_path(TypesInformedSearch.UNIFORM_COST, b, c)


# nodeA = Vertex("A")
# nodeB = Vertex("B")
# nodeC = Vertex("C")
# nodeD = Vertex("D")
# nodeE = Vertex("E")
# nodeF = Vertex("F")
# nodeG = Vertex("G")
# nodeH = Vertex("H")
# nodeI = Vertex("I")
# nodeJ = Vertex("J")
# nodeK = Vertex("K")
# nodeL = Vertex("L")
# nodeM = Vertex("M")
# nodeN = Vertex("N")
# nodeO = Vertex("O")
# nodeP = Vertex("P")
# nodeQ = Vertex("Q")

# nodeQ.add({nodeA: 1, nodeG: 12}, True)
# nodeA.add({nodeB: 3, nodeC: 1}, True)
# nodeB.add({nodeD: 3}, True)
# nodeC.add({nodeD: 1, nodeG: 2}, True)
# nodeD.add({nodeG: 3}, True)


# nodeA.add({nodeB: 168.5, nodeF: 144.63, nodeC: 318.71})
# nodeB.add({nodeC: 198.16, nodeD: 246.56, nodeF: 193.84})
# nodeC.add({nodeD: 142.34, nodeE: 140.04})
# nodeD.add({nodeG: 137.18, nodeF: 155.46})
# nodeE.add({nodeG: 289.11})

# g = Graph([nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG])
# g.show()
# g.show_shortest_path(TypesInformedSearch.DIJKSTRA, nodeG, nodeA)

# # Ejemplo 2
# nodeA.add({nodeB: 113})
# nodeB.add({nodeC: 65, nodeD: 66, nodeE: 49})
# nodeC.add({nodeI: 55})
# nodeD.add({nodeI: 97, nodeH: 94})
# nodeE.add({nodeF: 49})
# nodeF.add({nodeG: 45})
# nodeG.add({nodeH: 61, nodeL: 47})
# nodeH.add({nodeL: 63, nodeK: 49})
# nodeI.add({nodeJ: 55})
# nodeJ.add({nodeN: 102, nodeQ: 91})
# nodeK.add({nodeL: 50, nodeN: 54})
# nodeL.add({nodeN: 50})
# nodeM.add({nodeN: 157, nodeO: 210})
# nodeN.add({nodeP: 44, nodeO: 129})
# nodeO.add({nodeN: 129})
# nodeP.add({nodeQ: 68})

# g = Graph(
#     [
#         nodeA,
#         nodeB,
#         nodeC,
#         nodeD,
#         nodeE,
#         nodeF,
#         nodeG,
#         nodeH,
#         nodeI,
#         nodeJ,
#         nodeK,
#         nodeL,
#         nodeM,
#         nodeN,
#         nodeO,
#         nodeP,
#         nodeQ,
#     ]
# )
# g.show()
# g.show_shortest_path(TypesInformedSearch.DIJKSTRA, nodeK, nodeA)


# Ruta encontrada!!!
#         > Primero comienza en Q
#                 >Luego continua hacia P que tiene un costo de 68
#                 >Luego continua hacia N que tiene un costo de 112
#                 >Luego continua hacia L que tiene un costo de 162
#                 >Luego continua hacia G que tiene un costo de 209
#                 >Luego continua hacia F que tiene un costo de 254
#         > Y finaliza en E que tiene un costo de 303
