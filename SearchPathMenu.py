from Graph import Graph
from Menu import Menu
from TypesInformedSearch import TypesInformedSearch
from Vertex import Vertex


class SearchPathMenu(Menu):
    def __init__(self, title: str, options: list[str]):
        super().__init__(title, options)

    def interact(self, graph: Graph) -> None:

        super().interact()
        while not super().is_option_exit():
            menu = Menu(
                "Selecciona el vertice de inicio ",
                self.__update_options(graph.get_vertexs()),
            )
            menu.interact()
            while not menu.is_option_exit():
                menu2 = Menu(
                    f"El vértice de incio es '{graph.get_vertex(menu.get_option()-1)}' y el vértice final es: ",
                    self.__update_options(graph.get_vertexs()),
                )
                menu2.interact()
                if not menu2.is_option_exit():
                    graph.shortest_path_with_positions(
                        TypesInformedSearch.get(super().get_option() - 1),
                        menu.get_option(),
                        menu2.get_option(),
                    )
                    input()

                menu.interact()
            super().interact()

    def __update_options(self, vertexs: list[Vertex]) -> list[str]:
        result = []
        for i in vertexs:
            if i != "Volver":
                result.append(i)
        result.append("Volver")
        return result
