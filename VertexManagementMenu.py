from Vertex import Vertex
from Menu import Menu
from Console import Console


class VertexManagementMenu(Menu):
    def __init__(self, title: str, options: list[str]):
        super().__init__(title, options)
        self.__vertexs: list[Vertex] = []

    def interact(self) -> None:
        super().interact()

        while not super().is_option_exit():
            if super().is_option(1):
                self.__set_nodes()
                # if self.__exists_nodes():
            if super().is_option(2):
                self.__edit_nodes()
            if super().is_option(3):
                self.__delete_nodes()
            if super().is_option(4):
                self.__join_nodes()
            # else:
            # input("Debes ingresar por lo menos dos nodos!!!!. Presiona ENTER...")

            super().interact()

    def __set_nodes(self) -> None:
        is_exit = False
        while not is_exit:
            self.__vertexs.append(Vertex(Console.read_str(f"Nombre: ")))
            is_exit = not Console.is_yes("¿Deseas añadir mas nodos?(Y/n): ")

    def __edit_nodes(self) -> None:
        menu = Menu("Actualización de nodos", self.__update_options())
        menu.interact()
        while not menu.is_option_exit():
            node = self.__get_node(menu.get_option())
            print(f"Actualizar datos para '{node}'")
            node.set_name(input("Nombre: "))
            menu.interact()

    def __delete_nodes(self) -> None:
        menu = Menu("Eliminacion de nodos", self.__update_options())
        menu.interact()
        while not menu.is_option_exit():
            node = self.__get_node(menu.get_option())
            if Console.is_yes(
                f"¿Estás seguro de querer elimianr el nodo '{node}'? (Y/n): "
            ):
                self.__vertexs.remove(node)
                menu = Menu("Eliminacion de nodos", self.__update_options())
            menu.interact()

    def __join_nodes(self) -> None:
        menu = Menu("Unir nodos", self.__update_options())
        menu.interact()
        while not menu.is_option_exit():
            node1 = self.__get_node(menu.get_option())

            menu2 = Menu(
                f"Con cual nodo deseas unir el nodo {node1}",
                self.__update_options(),
            )
            menu2.interact()
            if not menu2.is_option_exit():
                node2 = self.__get_node(menu2.get_option())

                weight = 0
                if Console.is_yes("Deseas añadir peso? (Y/n): "):
                    weight = Console.read_int("Ingresa el peso: ")

                node1.add({node2: weight})
                print(f"Se ha unido '{node1}' con '{node2}' con un peso de {weight}")
                Console.read_str("Ingresa ENTER para continuar...")

            menu.interact()

    def __update_options(self) -> list[str]:
        result = []
        for i in self.__vertexs:
            if i != "Volver":
                result.append(i)
        self.__vertexs = result
        result.append("Volver")
        return result

    # def __exists_nodes(self) -> bool:
    #     return len(self.__nodes) > 1

    def get_vertexs(self) -> list[Vertex]:
        return self.__vertexs

    def __get_node(self, position: int) -> Vertex:
        return self.__vertexs[position - 1]
