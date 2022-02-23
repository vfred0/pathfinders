class Vertex:
    def __init__(self, value: str) -> None:
        self.__value = value
        self.__childrens = {}
        self.__parent: Vertex = None
        self.__cost = 0

    def contains(self, vertex) -> bool:
        return self.__childrens.__contains__(vertex)

    def add(self, vertexs: dict, directed: bool = False) -> None:
        for children, weight in vertexs.items():
            self.__childrens.update({children: weight})
            if not directed:
                children.__childrens.update({self: weight})

    def add_costs_for_childrens(self, check=None) -> list:
        childrens = []
        if self.__childrens:
            for vertex, cost in self.get_childrens():
                if vertex != check:
                    new_cost = cost + self.__cost
                    if vertex.__cost_is_infinite() or new_cost < vertex.__cost:
                        if vertex != self.__parent:
                            self.__set_cost_for(vertex, self, new_cost)
                            childrens.append(vertex)
        return childrens

    def __set_cost_for(self, vertex, parent, cost: int) -> None:
        vertex.__cost = cost
        vertex.__parent = parent

    def reset(self):
        self.__parent = None
        self.__cost = 0

    def get_childrens(self) -> dict:
        return self.__childrens.items()

    def get_child_keys(self) -> list:
        return list(self.__childrens.keys())

    def remove_childrens(self) -> None:
        if self.__childrens:
            for vertex in self.get_child_keys():
                del self.__childrens[vertex]

    def get_parents(self) -> list:
        result = []

        vertex = self
        while vertex:
            result.append(vertex)
            vertex = vertex.__parent
        return result

    def have_parent(self) -> bool:
        return self.__parent

    def get_parent(self):
        return self.__parent

    def get_value(self) -> str:
        return self.__value

    def get_cost(self) -> float:
        return round(self.__cost, 2)

    def set_name(self, name: str) -> None:
        self.__value = name

    def __cost_is_infinite(self) -> bool:
        return self.__cost == 0

    def __str__(self) -> str:
        return self.__value

    def __gt__(self, __o: object) -> bool:
        return self.__cost > __o.__cost
