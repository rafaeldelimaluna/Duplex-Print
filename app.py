from sys import argv
from Printer import Printer
from utils import Entries, Validator
from utils.prompt_gui import PromptGui


def MakeNormalPrint(filename=""):
    if filename == "":
        filename = input("Filename: ")
    output_filename_validated = Validator.file(filename)
    if not output_filename_validated:
        return False
    filename = output_filename_validated
    printquality = input(
        "| Print Quality[1,2,3]\n| [Rascunho,Normal,Melhor]\n| [Draft,Normal,Best]\n|\033[1;32m Qualidade:\033[0;37m ")
    duplex = True
    outputorder = True
    Printer(filename, duplex, printquality,
            outputorder, "A4", "CMD").Print()
    return True


def main() -> bool:
    args = argv[1:]
    if args.__len__() == 0:
        return False
    elif args[0] == "prompt_gui":
        return PromptGui().start()
    elif args[0] == "duplex normal":
        return MakeNormalPrint(args[1] if len(args) > 1 else "")
    elif args[0] == "iterable":
        Entries.iterable()


if __name__ == "__main__":
    if not main():
        print("No Arguments")
