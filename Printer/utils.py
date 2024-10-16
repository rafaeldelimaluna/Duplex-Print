from time import sleep
from subprocess import run
from gui import Question
from os import get_exec_path, getcwd, listdir, path


class Commands:
    pattern = "lpr"
    odd = []
    even = []


class Manager:
    def __init__(self, commands: tuple) -> None:
        self.commands = commands
        self.__question_obj = Question()

    def __verifyIfEnded(self) -> bool:
        run(args=['lpstat -W not-completed > .output.txt'], shell=True)
        r = open('.output.txt', 'r')
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
            if command_index == 1:
                if not self.__question_obj.start():
                    break
            run([command_initialize_print], shell=True)
            while True:
                i += 1
                if i > 400 or self.__verifyIfEnded():
                    break
                sleep(1)


class Interpreter:
    @staticmethod
    def print_quality(print_quality_value: int | str):
        match print_quality_value:
            case "3" | 3:
                return "Draft"
            case "4" | 4:
                return "Normal"
            case "5" | 5:
                return "Best"
            case _:
                return "Invalid"


class Directories:
    app_path = get_exec_path()[0].split('/')[:-2]
    app_path = '/'.join(app_path)
    blank_pdf = app_path+"/duplex-print/Printer/blank.pdf"
    cwd = getcwd()
    files_in_just_path = [file for file in listdir(cwd) if path.isfile(file)]
