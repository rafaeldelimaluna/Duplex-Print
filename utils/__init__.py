from time import sleep
from os import getcwd
from subprocess import run


class Commands:
    pattern = "lpr"
    odd = ""
    even = ""


class Manager:

    def __init__(self, commands: tuple) -> None:
        self.commands = commands

    def __verifyIfEnded(self) -> bool:
        run(args=['lpstat -W not-completed > output.txt'], shell=True)
        r = open('output.txt', 'r')
        output = r.read()
        if output == "":
            return True

    def __question(self):
        while True:
            run(['clear'])
            question = input(
                "A Primeira Parte já foi impressa!\nCertifique-se de que virou a folha para continuar\n---------------\nPode continuar?[y/n]").lower()

            match question:
                case "y" | "s":
                    return True
                case "n":
                    return False
                case _:
                    pass

    def Print(self):
        for command_index, command_initialize_print in enumerate(self.commands):
            i = 0
            run([command_initialize_print], shell=True)
            if command_index == 1:
                if not self.__question():
                    break
            while True:
                i += 1
                if i > 400 or self.__verifyIfEnded():
                    break
                sleep(1)


class Interpreter:
    @staticmethod
    def print_quality(print_quality_value: int | str):
        match print_quality_value:
            case 3:
                return "Draft"
            case 4:
                return "Normal"
            case 5:
                "Best"
            case _:
                return "Invalid"
