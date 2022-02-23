import datetime
from abc import ABC, abstractmethod
from Vertex import Vertex
from TypesInformedSearch import TypesInformedSearch


class InformedSearch(ABC):
    def __init__(self, start: Vertex, goal: Vertex) -> None:
        self.__start = start
        self.__goal = goal
        self.__times = {}

    def shortest_path(self):
        start_time = datetime.datetime.now()
        iterations = 1
        visited_vertex = self.__start
        children_of_vertexs_visited: list[Vertex] = self.__sorted(
            visited_vertex.add_costs_for_childrens()
        )
        self.__show(iterations, visited_vertex, children_of_vertexs_visited)

        while self._search_condition(children_of_vertexs_visited):
            iterations += 1
            visited_vertex = children_of_vertexs_visited[0]
            children_of_vertexs_visited.remove(visited_vertex)
            self.__show(iterations, visited_vertex, children_of_vertexs_visited)
            for vertex in visited_vertex.add_costs_for_childrens(self.__start):
                children_of_vertexs_visited.append(vertex)

            children_of_vertexs_visited = self.__sorted((children_of_vertexs_visited))

        end_time = datetime.datetime.now()

        time_diff = end_time - start_time
        execution_time = time_diff.total_seconds() * 1000
        print(">>>Resultados<<<")
        print(f"Número de iteraciones: {iterations}")
        print(f"Tiempo de ejecución: {execution_time:.3f}ms")

    def __sorted(self, vertexs: list[Vertex]) -> list[Vertex]:
        return sorted(vertexs, key=lambda vertex: vertex)

    def __show(
        self,
        iterations: int,
        visited_vertex: Vertex,
        vertexs: list[Vertex],
    ) -> None:
        print(f"ANALIZAR: {visited_vertex} ITERACION: {iterations} ")
        for i in vertexs:
            print(f"EN COLA {i} -> {i.get_parent()}: {i.get_cost()}")
        print("###################")

    @abstractmethod
    def _search_condition(self, children_of_vertexs_visited: list[Vertex]) -> bool:
        pass

    def _show_path(self, only_last_cost: bool = False) -> None:
        if self.exists_route():
            cost = 0
            vertexs = self.get_route()
            start, goal = vertexs[0], vertexs[-1]

            cost = goal.get_cost()

            print(f"Ruta encontrada!!!")
            print(f"\t> Primero comienza en {start}")

            for vertex in vertexs[1:-1]:
                print(
                    f"\t\t>Luego continua hacia {vertex} que tiene un costo de {vertex.get_cost()}"
                )
                cost += vertex.get_cost()
            print(f"\t> Y finaliza en {goal} que tiene un costo de {goal.get_cost()}")
            if only_last_cost:
                cost = goal.get_cost()
            print(f"Total costo: {cost}")
        else:
            print(
                f"No se ha encontrado una ruta para ir de {self.__start} a {self.__goal}"
            )

    def get_goal(self) -> Vertex:
        return self.__goal

    def get_route(self) -> list[Vertex]:
        return list(self.__goal.get_parents().__reversed__())

    def exists_route(self) -> bool:
        return self.__goal.have_parent()

    def _get_start(self) -> Vertex:
        return self.__start
