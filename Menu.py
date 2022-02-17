from typing import List
from Console import Console


class Menu:
    def __init__(self, title: str, options: list[str]):
        self.__title = title
        self.__options = options
        self.__option = 0

    def interact(self) -> None:
        Console.clean_screen()
        self.__show()
        self.__option = Console.read_int(
            f"Ingresa una opcion del 1 al {len(self.__options)}: "
        )
        while not self.__is_valid(self.__option):
            print(f"La opcion ingresada no es válida")
            self.__option = Console.read_int(
                f"Ingresa una opcion del 1 al {len(self.__options)}: "
            )

    def __is_valid(self, option: int) -> bool:
        return option > 0 and option <= len(self.__options)

    def __show(self) -> None:
        print(self.__title)
        for index, value in enumerate(self.__options):
            print(f"{index+1}. {value}")

    def is_option_exit(self) -> bool:
        return self.__option == len(self.__options)

    def is_option(self, option: int) -> bool:
        return self.__option == option

    def get_option(self) -> int:
        return self.__option
