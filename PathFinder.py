from Menu import Menu
from SearchPathMenu import SearchPathMenu
from TypesInformedSearch import TypesInformedSearch
from Vertex import Vertex
from VertexManagementMenu import VertexManagementMenu
from Graph import Graph


class PathFinder:
    def __init__(self) -> None:
        self.__vertexs: list[Vertex] = []
        self.__graph: Graph = None
        self.__type_search_informed: TypesInformedSearch = None
        self.__menus: list[Menu] = [
            Menu(
                "Buscador de rutas",
                [
                    "Gestión de vértices",
                    "Dibujar grafo",
                    "Búsqueda de la ruta más corta",
                    "Salir",
                ],
            ),
            VertexManagementMenu(
                "Gestión de vértices",
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
                self.__vertexs = vertex_menu.get_vertexs()
                is_back = vertex_menu.is_option_exit()
            if main_menu.is_option(2):
                self.__graph = Graph(self.__vertexs[0])
                self.__graph.show()
                input("Revisa la carpeta out...")
            if main_menu.is_option(3):
                search_menu = self.__menus[main_menu.get_option() - 1]
                search_menu.interact(self.__vertexs)
                self.__graph.show_shortest_path(
                    search_menu.get_option() - 1,
                    search_menu.get_start(),
                    search_menu.get_goal(),
                )
                is_back = vertex_menu.is_option_exit()

            if is_back:
                main_menu.interact()


PathFinder().interact()
