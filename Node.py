class Node:
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
            for node, weight in self.get_childrens():
                new_cost = weight + self.__cost
                if node != self and node.__cost_is_infinite() or new_cost < node.__cost:
                    node.__cost = new_cost
                    node.__parent = self
                del node.__childrens[self]

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

    def get_cost(self):
        return self.__cost

    def set_name(self, name: str) -> None:
        self.__value = name

    def __cost_is_infinite(self) -> bool:
        return self.__cost == 0

    def __str__(self) -> str:
        return self.__value

    def __gt__(self, __o: object) -> bool:
        return self.__cost > __o.__cost
