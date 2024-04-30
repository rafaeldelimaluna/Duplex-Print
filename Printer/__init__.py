from pypdf import PdfReader, PdfWriter
from Printer.utils import Manager, Commands, Interpreter
from os import getcwd, remove, path


class Printer(Manager):
    def __init__(self, filename, duplex: bool, print_quality: int | str, print_reversed: bool, media_size: str, job_name="") -> None:
        self.duplex = "duplex" if duplex else None
        self.__is_duplex = duplex
        self.__cwd = getcwd()
        self.file_target = self.__cwd+'/' + filename
        self.filename = filename
        self.oprint_quality = self.__convertPrintQualityEntryToCupsEntry(
            print_quality)
        self.print_quality_text = Interpreter.print_quality(
            self.oprint_quality)
        self.omedia = media_size if media_size != "" else None
        self.ooutputorder = "reversed" if print_reversed else None
        self.T = None if job_name == "" else job_name
        self.pdf = PdfReader(self.filename)
        self.pdf_len = len(self.pdf.pages)
        self.cups_command = self.__createCupsCommand()
        self.relatory = self.__MakePrintRelatory()
        super().__init__(self.cups_command)

    def __convertPrintQualityEntryToCupsEntry(self, print_quality_entry):
        """# Qualidades vs Cups
        A Qualidade é ascendente, sendo:\n
        1 - Rascunho\n
        2 - Normal\n
        3 - Melhor\n
        print_quality -- Retorna a qualidade que irá funcionar no CUPS
        Return: print_quality +2
        """
        if isinstance(print_quality_entry, int):
            return print_quality_entry+2

        print_quality_entry = print_quality_entry.lower()
        match print_quality_entry:
            case "draft" | "rascunho":
                return 3
            case "normal":
                return 4
            case "best" | "melhor":
                return 5

    def __createDuplexCommandPrint(self, even: bool):
        # output = Commands.pattern + f" -o pages-ranges={pages} {self.filename}"
        writer = PdfWriter()
        output = Commands.pattern + " "
        filename = ".even-29042024.pdf" if even else ".odd-29042024.pdf"
        [writer.add_page(self.pdf.pages[i])
            for i in range(even, self.pdf_len, 2)]
        writer.write(filename)
        if even:
            output += ".even-29042024.pdf"
            return output
        else:
            output += '.odd-29042024.pdf'
            return output

    def __MakePrintRelatory(self) -> dict:
        relatory_data = dict()
        relatory_data["Title"] = self.T
        relatory_data["File target"] = self.filename
        relatory_data["Media"] = self.omedia
        relatory_data["Output order"] = self.ooutputorder
        relatory_data["Print Quality"] = self.print_quality_text
        return relatory_data

    def __createCupsCommand(self) -> tuple:
        command = "lpr -U rafae"
        if self.omedia != None:
            command += f" -o media={self.omedia}"
        if self.oprint_quality != None:
            command += f" -o print-quality={self.oprint_quality}"
        if self.ooutputorder != None:
            command += f" -o outputorder={self.ooutputorder}"
        if self.T != None:
            command += f" -T {self.T}"
        Commands.pattern = command
        if self.duplex:
            Commands.odd = self.__createDuplexCommandPrint(False)
            Commands.even = self.__createDuplexCommandPrint(True)
            return (Commands.odd, Commands.even)
        print(Commands.odd)
        print(Commands.even)
        command += f" {self.filename}"
        return (command)

    def Print(self):
        print(self.relatory)
        super().Print()
        if self.__is_duplex:
            if path.exists('.even-29042024.pdf'):
                remove(".even-29042024.pdf")
            if path.exists('.odd-29042024.pdf'):
                remove('.odd-29042024.pdf')
