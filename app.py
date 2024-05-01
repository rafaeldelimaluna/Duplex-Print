from sys import argv
from Printer import Printer
from utils import Entries, Validator


def start() -> bool:
    args = argv[1:]
    # print('filename | duplex[s|n] | reversed | printquality')
    # print(args)
    if args.__len__() == 0:
        return False
    elif args[0] == "duplex normal":
        filename = input("Filename: ")
        output_filename_validated = Validator.file(filename)
        if not output_filename_validated:
            return False
        filename = output_filename_validated
        printquality = input(
            "Print Quality[1,2,3] | [Rascunho,Normal,Melhor] | [Draft,Normal,Best]: ")
        duplex = True
        outputorder = True
        Printer(filename, duplex, printquality,
                outputorder, "A4", "CMD").Print()
    elif args[0] == "iterable":
        Entries.iterable()


if __name__ == "__main__":
    if not start():
        print("No Arguments")
