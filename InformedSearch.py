from abc import ABC, abstractmethod
from Node import Node
from TypesInformedSearch import TypesInformedSearch


class InformedSearch(ABC):
    def __init__(self, start: Node, goal: Node) -> None:
        # self.__types_informed_search = types_informed_search
        self.__start = start
        self.__goal = goal

    def shortest_path(self):
        visited_node = self.__start
        visited_node.set_cost_for_childrens()
        children_of_nodes_visited: list[Node] = visited_node.get_child_keys()
        while self._search_condition(children_of_nodes_visited):
            visited_node = children_of_nodes_visited[0]
            children_of_nodes_visited.remove(visited_node)
            visited_node.set_cost_for_childrens()
            for node in visited_node.get_child_keys():
                children_of_nodes_visited.append(node)

            children_of_nodes_visited = sorted(
                list(set(children_of_nodes_visited)),
                key=lambda node: node,
            )

    @abstractmethod
    def _search_condition(self, children_of_nodes_visited: list[Node]) -> bool:
        pass

    def _show_path(self, only_last_cost: bool = False) -> None:
        if self.__goal.have_parent():
            cost = 0
            nodes = self.get_route()
            start, goal = nodes[0], nodes[-1]
            cost = goal.get_cost()

            print(f"Ruta encontrada!!!")
            print(f"\t> Primero comienza en {start}")

            for node in nodes[1:-1]:
                print(
                    f"\t\t>Luego continua hacia {node} que tiene un costo de {round(node.get_cost(), 2)}"
                )
                if not only_last_cost:
                    cost += node.get_cost()
            print(
                f"\t> Y finaliza en {goal} tiene un costo de {round(goal.get_cost(), 2)}"
            )
            cost += goal.get_cost()
            print(f"Total costo: {round(cost, 2)}")
        else:
            print(
                f"No se ha encontrado una ruta para ir de {self.__start} a {self.__goal}"
            )

    def get_goal(self) -> Node:
        return self.__goal

    def get_route(self) -> list[Node]:
        return list(self.__goal.get_parents().__reversed__())
