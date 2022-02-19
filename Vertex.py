class Vertex:
    def __init__(self, value: str) -> None:
        self.__value = value
        self.__childrens = {}
        self.__parent = None
        self.__cost = 0

    def contains(self, node) -> bool:
        return self.__childrens.get(node)

    def add(self, nodes: dict, directed: bool = False) -> None:
        for children, weight in nodes.items():
            self.__childrens.update({children: weight})
            if not directed:
                children.__childrens.update({self: weight})

    def set_cost_for_childrens(self) -> None:
        if self.__childrens:
            for vertex, cost in self.get_childrens():
                if vertex != self:
                    new_cost = cost + self.__cost
                    if vertex.__cost_is_infinite() or new_cost < vertex.__cost:
                        self.__set_cost(vertex, self, new_cost)
                    vertex.__delete(self)

    def __set_cost(self, vertex, parent, cost: int) -> None:
        vertex.__cost = cost
        vertex.__parent = parent

    def __delete(self, node) -> None:

        if node and self.contains(node):
            del self.__childrens[node]

    def get_childrens(self) -> dict:
        return self.__childrens.items()

    def get_child_keys(self) -> list:
        return list(self.__childrens.keys())

    def get_parents(self) -> list:

        result = []
        node = self
        while node:
            result.append(node)
            node = node.__parent
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
