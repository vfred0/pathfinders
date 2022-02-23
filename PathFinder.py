from Graph import Graph
from Menu import Menu
from SearchPathMenu import SearchPathMenu
from TypesInformedSearch import TypesInformedSearch
from VertexManagementMenu import VertexManagementMenu


class PathFinder:
    def __init__(self) -> None:
        self.__graph: Graph = None
        self.__menus: list[Menu] = [
            Menu(
                "Buscador de rutas",
                [
                    "Gestión del grafo",
                    "Búsqueda de la ruta más corta",
                    "Salir",
                ],
            ),
            VertexManagementMenu(
                "Gestión del grafo",
                [
                    "Ingreso de vértice",
                    "Actualización de vértice",
                    "Eliminación de vértice",
                    "Unir vértices",
                    "Volver",
                ],
            ),
            SearchPathMenu(
                "Búsqueda de la ruta más corta",
                [
                    TypesInformedSearch.get(0),
                    TypesInformedSearch.get(1),
                    "Volver",
                ],
            ),
        ]

    def interact(self):
        main_menu = self.__menus[0]
        main_menu.interact()
        is_back = False
        while not main_menu.is_option_exit():
            if main_menu.is_option(1):
                vertex_menu = self.__menus[1]
                vertex_menu.interact()
                self.__graph = vertex_menu.get_graph()
                is_back = vertex_menu.is_option_exit()
            if main_menu.is_option(2):
                search_menu = self.__menus[main_menu.get_option()]
                if self.__graph:
                    search_menu.interact(self.__graph)
                    is_back = search_menu.is_option_exit()
                else:
                    input("Error!!! No hay grafo...")
                    is_back = True

            if is_back:
                main_menu.interact()


PathFinder().interact()
