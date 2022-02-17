from enum import Enum, auto


class TypesInformedSearch(Enum):
    DIJKSTRA = auto()
    UNIFORM_COST = auto()

    def is_dijkstra(self) -> bool:
        return self == TypesInformedSearch.DIJKSTRA

    def is_uniform_cost(self) -> bool:
        return self == TypesInformedSearch.UNIFORM_COST
