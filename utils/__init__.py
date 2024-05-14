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
        duplex = Entries.__questionTrueOrFalse("duplex[s/n]: ")
        outputorder = Entries.__questionTrueOrFalse("Inversed[s/n]: ")
        printquality = input(
            "Print Quality[1,2,3] | [Rascunho,Normal,Melhor] | [Draft,Normal,Best]: ")
        output_filename_validated = Validator.file(filename)
        if not output_filename_validated:
            return False
        Printer(output_filename_validated, duplex, printquality,
                outputorder, media, "").Print()


class Validator:
    @staticmethod
    def __filepath(filename) -> str:
        filename_pdf = f"{filename}.pdf"
        if path.exists(filename):
            return filename
        elif path.exists(filename_pdf):
            return filename_pdf
        return False

    @staticmethod
    def file(filename) -> str | bool:
        output_filepath = Validator.__filepath(filename)
        if not output_filepath:
            return False
        return output_filepath
