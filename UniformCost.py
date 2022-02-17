from InformedSearch import InformedSearch
from Node import Node


class UniformCost(InformedSearch):
    def __init__(self, start: Node, goal: Node) -> None:
        super().__init__(start, goal)

    def _search_condition(self, children_of_nodes_visited: list[Node]) -> bool:
        return (
            children_of_nodes_visited[0] != self.get_goal()
            and children_of_nodes_visited
        )

    def shortest_path(self):
        super().shortest_path()
        super()._show_path(True)


# nodeA = Node("A")
# nodeB = Node("B")
# nodeC = Node("C")
# nodeD = Node("D")
# nodeE = Node("E")
# nodeF = Node("F")
# nodeG = Node("G")


# nodeA.add({nodeB: 168.5, nodeF: 144.63, nodeC: 318.71})
# nodeB.add({nodeC: 198.16, nodeD: 246.56, nodeF: 193.84})
# nodeC.add({nodeD: 142.34, nodeE: 140.04})
# nodeD.add({nodeG: 137.18, nodeF: 155.46})
# nodeE.add({nodeG: 289.11})

# UniformCost(nodeA, nodeG).shortest_path()
# ca = Node("Cadiz")
# se = Node("Sevilla")
# ja = Node("Jaen")
# gr = Node("Granada")
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

# ca.add({se: 125})
# se.add({ja: 242, gr: 256})
# ja.add({a7: 335, gr: 99})
# gr.add({a6: 278})
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
# # UniformCost().shortest_path(a12, gr)
