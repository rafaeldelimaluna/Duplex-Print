from pypdf import PdfReader, PdfWriter
from Printer.utils import Manager, Commands, Interpreter, Directories
from os import getcwd, remove, path


class Printer(Manager):
    def __init__(self, filename, duplex: bool = False, print_quality: int | str = 0, print_reversed: bool = True, media_size: str = "A4", job_name: str = "Duplex_Print") -> None:
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
        self.T = ("inherited" if job_name ==
                  "" else job_name).replace(' ', '_')
        self.__blank_pdf = PdfReader(Directories.blank_pdf)
        self.pdf = PdfReader(self.filename)
        self.pdf_len = self.pdf.get_num_pages()
        self.cups_command = self.__createCupsCommand()
        self.relatory = self.__MakePrintRelatory()
        super().__init__(self.cups_command)

    def __convertPrintQualityEntryToCupsEntry(self, print_quality_entry):
        """# Qualidades vs Cups
        A Qualidade é ascendente, sendo:\n
        1 - Rascunho\n
        2 - Normal\n
        3 - Melhor\n
        print_quality -- Retorna a qualidade que será enviada pelo comando no CUPS
        Return: print_quality +2
        """
        print_quality_entry = print_quality_entry.lower()
        match print_quality_entry:
            case "draft" | "rascunho" | "1":
                return 3
            case "normal" | "2":
                return 4
            case "best" | "melhor" | "3":
                return 5

    def __makeFile(self, filename, even):
        writer = PdfWriter()
        for i in range(even, self.pdf_len, 2):
            writer.add_page(self.pdf.pages[i])
        if even and self.pdf_len % 2 != 0:
            writer.add_page(self.__blank_pdf.get_page(0))
            print('colocado em even')
        writer.write(filename)

    def __createDuplexCommandPrint(self, even: bool):
        filename = ".even-29042024.pdf" if even else ".odd-29042024.pdf"
        output = Commands.pattern + " "
        self.__makeFile(filename, even)
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
        relatory_data["Total Number Pages"] = self.pdf_len
        return relatory_data

    def __printRelatory(self):
        print(f"\033[7;32m| {'Titulo':^20}| {'Valor':^50}|\033[m")
        # print(f"{'-'*45}")
        for key in self.relatory:
            print(f"\033[4m| {key:^20}| {self.relatory[key]:^50}|\033[m")

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
        command += f" {self.filename}"
        return (command)

    def __removeTemporaryFiles(self) -> None:
        """Remove os arquivos temporários criados durante a execução da impressão"""
        if path.exists('.even-29042024.pdf'):
            remove(".even-29042024.pdf")
        if path.exists('.odd-29042024.pdf'):
            remove('.odd-29042024.pdf')
        if path.exists('.output.txt'):
            remove('.output.txt')

    def Print(self):
        self.__printRelatory()
        super().Print()
        if self.__is_duplex:
            self.__removeTemporaryFiles()
