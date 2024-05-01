from Printer import Printer
from os import path


class Entries:
    @staticmethod
    def __questionTrueOrFalse(question: str) -> bool:
        while True:
            entry = input(question).lower()
            match entry:
                case "y" | "s" | "sim" | "yes":
                    return True
                case "n" | "not" | "nao":
                    return False
                case _:
                    pass

    @staticmethod
    def iterable():
        filename = input("File target: ")
        media = input("Media: ")
        duplex = Entries.__questionTrueOrFalse("duplex[y/s]: ")
        outputorder = Entries.__questionTrueOrFalse("Duplex[y/n]: ")
        printquality = input(
            "Print Quality[1,2,3] | [Rascunho,Normal,Melhor] | [Draft,Normal,Best]: ")
        Printer(filename, duplex, printquality,
                outputorder, media, "").Print()


class Validator:
    @staticmethod
    def file(filename) -> str | bool:
        filename_pdf = f"{filename}.pdf"

        def filepath() -> str:
            if path.exists(filename):
                return filename_pdf
            elif path.exists(filename_pdf):
                return filename_pdf
            return False
        output_filepath = filepath()
        if (filename).count(' ') > 0:
            print(f"Muitos espaços no nome do arquivo [{filename}]")
            return False
        if not output_filepath:
            return False
        return output_filepath
