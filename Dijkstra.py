from InformedSearch import InformedSearch
from Node import Node


class Dijkstra(InformedSearch):
    def __init__(self, start: Node, goal: Node) -> None:
        super().__init__(start, goal)

    def _search_condition(self, children_of_nodes_visited: list[Node]) -> bool:
        return children_of_nodes_visited

    def shortest_path(self):
        super().shortest_path()
        super()._show_path()

    # def show_path(self, goal: Node) -> None:
    #     goal.show_parents()


# nodeA = Node("A")
# nodeB = Node("B")
# nodeC = Node("C")
# nodeD = Node("D")
# nodeE = Node("E")
# nodeF = Node("F")
# nodeG = Node("G")
# nodeH = Node("H")
# nodeI = Node("I")
# nodeJ = Node("J")
# nodeK = Node("K")
# nodeL = Node("L")
# nodeM = Node("M")
# nodeN = Node("N")
# nodeO = Node("O")
# nodeP = Node("P")
# nodeQ = Node("Q")

# nodeC1 = Node("C1")
# nodeC2 = Node("C2")

# # Ejemplo 1
# nodeA.add({nodeB: 10, nodeC: 8, nodeD: 15})
# nodeB.add({nodeE: 15})
# nodeC.add({nodeG: 15, nodeJ: 14})
# nodeD.add({nodeG: 6, nodeI: 15})
# nodeE.add({nodeJ: 8, nodeH: 30})
# nodeF.add({nodeL: 15})
# nodeG.add({nodeF: 8, nodeI: 7})
# nodeH.add({nodeL: 15})
# nodeI.add({nodeK: 10})
# nodeJ.add({nodeH: 18, nodeF: 9})
# nodeK.add({nodeL: 10})


# # nodeA.add({nodeB: 168.5, nodeF: 144.63, nodeC: 318.71})
# # nodeB.add({nodeC: 198.16, nodeD: 246.56, nodeF: 193.84})
# # nodeC.add({nodeD: 142.34, nodeE: 140.04})
# # nodeD.add({nodeG: 137.18, nodeF: 155.46})
# # nodeE.add({nodeG: 289.11})


# Dijkstra(nodeA, nodeE).shortest_path()


# # Ejemplo 2
# # nodeA.add({nodeB: 113})
# # nodeB.add({nodeC: 65, nodeD: 66, nodeE: 49})
# # nodeC.add({nodeI: 55})
# # nodeD.add({nodeI: 97, nodeH: 94})
# # nodeE.add({nodeF: 49})
# # nodeF.add({nodeG: 45})
# # nodeG.add({nodeH: 61, nodeL: 47})
# # nodeH.add({nodeL: 63, nodeK: 49})
# # nodeI.add({nodeJ: 55})
# # nodeJ.add({nodeN: 102, nodeQ: 91})
# # nodeK.add({nodeL: 50, nodeN: 54})
# # nodeL.add({nodeN: 50})
# # nodeM.add({nodeN: 157, nodeO: 210})
# # nodeN.add({nodeP: 44, nodeO: 129})
# # # nodeO.add({nodeN: 129})
# # nodeP.add({nodeQ: 68})

# # Dijkstra().shortest_path(nodeK, nodeA)

# a1 = Node("Cadiz")
# a2 = Node("Sevilla")
# a3 = Node("Jaen")
# a4 = Node("Granada")
# a5 = Node("Albacete")
# a6 = Node("Murcia")
# a7 = Node("Madrid")
# a8 = Node("Valencia")
# a9 = Node("Barcelona")
# a10 = Node("Gerona")
# a11 = Node("Zaragoza")
# a12 = Node("Bilbao")
# a13 = Node("Oviedo")
# a14 = Node("Coruña")
# a15 = Node("Vigo")
# a16 = Node("Valladolid")
# a17 = Node("Badajoz")

# a1.add({a2: 125})
# a2.add({a3: 242, a4: 256})
# a3.add({a7: 335, a4: 99})
# a4.add({a6: 278})
# a5.add({a8: 191})
# a6.add({a8: 241, a5: 150})
# a7.add({a5: 251, a17: 403, a11: 325, a12: 395})
# a8.add({a9: 349})
# a9.add({a10: 100})
# a9.add({a11: 296})
# a11.add({a12: 324})
# a12.add({a13: 304})
# a16.add({a7: 193, a12: 280, a14: 455, a15: 356})
# a15.add({a14: 171})
