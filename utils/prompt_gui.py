from Printer import Directories
from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit import HTML
from prompt_toolkit.styles import Style
from pypdf import PdfReader
from Printer import Printer
from utils import clear_console


class PromptGui():
    files: list
    __styles_file = Style.from_dict({
        "h1": "#0015ff bold",
        'back': '#0015ff bg:#1C1018 bold',
        "dialog": "bg:#1C1018",
        "dialog.body": "bg:#fff #000",
        'dialog shadow': "bg:#355B80"
    })

    __styles_qualidade = Style.from_dict({
        "h1": "#ff0000 bold",
        "back": "#ff0000 bold",
        "dialog": "bg:#1C1018",
        "item": "bold",
        "dialog.body": "bg:#fff #000",
        'dialog shadow': "bg:#a36262"
    })
    files = [(file, f"{file:<20} | {PdfReader(file).get_num_pages()}")
             for file in Directories.files_in_just_path]
    clear_console()
    files.sort(reverse=True)
    files.append(("back", HTML("<h1>Sair</h1>")))
    qualidades = [("1", HTML("<item>1-Rascunho</item>")), ("2", HTML("<item>2-Normal</item>")),
                  ("3", HTML("<item>3-Melhor</item>")), (4, "Voltar"), (5, HTML("<back>Sair</back>"))]

    def __init__(self, file: str = ""):
        self.file: str = file
        self.qualidade: str = ""

    def __setFile(self):
        title = HTML("<h1>Duplex Print</h1>")
        self.file = radiolist_dialog(title=title,
                                     text="Escolha o arquivo a ser impresso", values=PromptGui.files, style=PromptGui.__styles_file).run()
        if self.file == "back":
            return False
        self.__setQualidade()

    def __setQualidade(self):
        self.qualidade = radiolist_dialog(
            title=self.file, text="Escolha a qualidade de impressão", values=PromptGui.qualidades, style=PromptGui.__styles_qualidade).run()
        if self.qualidade == 4:
            self.__setFile()
        elif self.qualidade == 5:
            return False
        return True

    def start(self):
        output = self.__setFile() if self.file == "" else self.__setQualidade()
        Printer(self.file, True, self.qualidade,
                True, "A4", "Prompt Gui").Print()
        return output
