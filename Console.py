import os


class Console:
    @staticmethod
    def read_str(message: str) -> int:
        result = str(input(message))

        while not all(i.isalnum() or i.isspace() for i in result):
            print(f"Error!!!. El caracter ingresado '{result}' no son letras")
            result = str(input(message))
        return result

    @staticmethod
    def read_int(message: str) -> int:
        result = input(message)
        while not result.isnumeric():
            print(f"Error!!!. El caracter ingresado '{result}' no es un número")
            result = input(message)
        return int(result)

    @staticmethod
    def read_number(message: str) -> float:
        result = input(message)
        while not Console.__is_float(result):
            print(f"Error!!!. El caracter ingresado '{result}' no es un número")
            result = input(message)
        return result

    @staticmethod
    def is_yes(message: str) -> bool:
        result = str(input(message))

        while not result == "" and not result == "y" and not result == "n":
            print(f"Error!!!. El caracter ingresado '{result}' es y o n")
            result = str(input(message))        
        return result == "y" or result == ""

    def __is_float(n) -> bool:
        try:
            float(n)
        except ValueError:
            return False
        return True

    @staticmethod
    def clean_screen():
        os.system("clear" if os.name == "posix" else "cls")


# Console.read_str("sjY/n): ")

# print(Console.is_yes("Si o no??? "))
# print("1".isalnum())
# print(len(" "))
