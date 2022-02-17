from Menu import Menu
from NodeManagementMenu import NodeManagementMenu


class GraphManagement:
    def __init__(self) -> None:
        self.__menus: list[Menu] = [
            Menu(
                "Grafos",
                [
                    "Gestión de nodos",
                    "Mostrar grafo",
                    "Buscar la ruta corta",
                    "Salir",
                ],
            ),
            NodeManagementMenu(
                "Gestion de nodos",
                [
                    "Ingreso de nodos",
                    "Actualización de nodos",
                    "Eliminación de nodos",
                    "Unir nodos",
                    "Volver ",
                ],
            ),
        ]

    def interact(self):
        main_menu = self.__menus[0]
        main_menu.interact()
        is_back = False
        while not main_menu.is_option_exit():
            if main_menu.is_option(1):
                node_menu = self.__menus[1]
                node_menu.interact()
                is_back = node_menu.is_option_exit()
            if main_menu.is_option(2):
                self.__show_graph()
            if main_menu.is_option(3):
                self.__search_shortest_path()

            if is_back:
                main_menu.interact()


GraphManagement().interact()
