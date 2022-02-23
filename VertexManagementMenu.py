from Graph import Graph
from Vertex import Vertex
from Menu import Menu
from Console import Console


class VertexManagementMenu(Menu):
    def __init__(self, title: str, options: list[str]):
        super().__init__(title, options)
        self.__vertexs: list[Vertex] = []
        self.__graph = None

    def interact(self) -> None:
        super().interact()

        while not super().is_option_exit():
            if super().is_option(1):
                self.__set_vertexs()
                # if self.__exists_vertexs():
            if super().is_option(2):
                self.__update_vertexs()
            if super().is_option(3):
                self.__delete_vertexs()
            if super().is_option(4):
                self.__join_vertexs()

            # else:
            # input("Debes ingresar por lo menos dos vértices!!!!. Presiona ENTER...")

            super().interact()

    def __update_graph(self) -> None:
        self.__graph = Graph(self.__vertexs)
        self.__graph.show()

    def __set_vertexs(self) -> None:
        is_exit = False
        while not is_exit:
            vertex = Vertex(Console.read_str(f"Nombre: "))
            if not self.__exists(vertex):
                self.__vertexs.append(vertex)
            self.__update_graph()
            is_exit = not Console.is_yes("¿Deseas añadir mas vértices?(Y/n): ")

    def __update_vertexs(self) -> None:
        menu = Menu("Actualización de vértices", self.__options())
        menu.interact()
        while not menu.is_option_exit():
            vertex = self.__get_vertex(menu.get_option())
            print(f"Actualizar datos para '{vertex}'")
            new_vertex = Vertex(Console.read_str(f"Nombre: "))
            if not self.__exists(new_vertex):
                vertex.set_name(new_vertex.get_value())
            self.__update_graph()
            menu.interact()

    def __delete_vertexs(self) -> None:
        menu = Menu("Eliminacion de vértices", self.__options())
        menu.interact()
        while not menu.is_option_exit():
            vertex = self.__get_vertex(menu.get_option())
            if Console.is_yes(
                f"¿Estás seguro de querer elimianr el vértice '{vertex}'? (Y/n): "
            ):
                vertex.remove_childrens()
                self.__vertexs.remove(vertex)

                menu = Menu("Eliminacion de vértices", self.__options())
            self.__update_graph()
            menu.interact()

    def __join_vertexs(self) -> None:
        menu = Menu("Unir vértices", self.__options())
        menu.interact()
        while not menu.is_option_exit():
            vertexA = self.__get_vertex(menu.get_option())

            menu2 = Menu(
                f"Con cual vértice deseas unir el vértice {vertexA}",
                self.__options(),
            )
            menu2.interact()
            if not menu2.is_option_exit():
                vertexB = self.__get_vertex(menu2.get_option())

                weight = 0
                if Console.is_yes("Deseas añadir peso? (Y/n): "):
                    weight = Console.read_int("Ingresa el peso: ")

                vertexA.add({vertexB: weight}, Console.is_yes("No Dirigido? (Y/n): "))
                print(
                    f"Se ha unido '{vertexA}' con '{vertexB}' con un peso de {weight}"
                )
                self.__update_graph()
                Console.read_str("Ingresa ENTER para continuar...")
            menu.interact()

    def __options(self) -> list[str]:
        result = []
        for i in self.__vertexs:
            if i != "Volver":
                result.append(i)
        result.append("Volver")
        return result

    def __exists(self, vertex: Vertex) -> bool:
        for i in self.__vertexs:
            if i.get_value() == vertex.get_value():
                return True
        return False

    def get_graph(self) -> Graph:
        return self.__graph

    def __get_vertex(self, position: int) -> Vertex:
        return self.__vertexs[position - 1]
