from Printer import Printer


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
