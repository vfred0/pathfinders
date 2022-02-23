from enum import Enum, auto


class TypesInformedSearch(Enum):
    DIJKSTRA = "Dijkstra"
    UNIFORM_COST = "Costo Uniforme"

    def is_dijkstra(self) -> bool:
        return self == TypesInformedSearch.DIJKSTRA

    def is_uniform_cost(self) -> bool:
        return self == TypesInformedSearch.UNIFORM_COST

    def all() -> list:
        return [i for i in TypesInformedSearch]

    def get(position: int):
        return TypesInformedSearch.all()[position]

    def __str__(self) -> str:
        return self._value_
