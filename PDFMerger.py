import os
from PyPDF2 import PdfFileMerger
import give_console_width

# Console width of the current/active console.
CONSOLE_WIDTH = give_console_width.main()

# Title of the program.
TITLE = "Hi! Welcome to your Image to PDF converter!"

# Developer.
THANKS_TO = "Developed by Camilo Martínez"

def clear() -> None:
    """ Clears the console.
    """
    if os.name == 'nt':
        _ = os.system('cls')  # For windows.
    else:
        _ = os.system('clear')  # For mac and linux (here, os.name is 'posix').

def show_introduction() -> None:
    """ Shows introduction of the program.
    """
    print("~" * CONSOLE_WIDTH)
    print("")
    print(" " * int(str((CONSOLE_WIDTH - len(TITLE))//2)) +
          TITLE + " " * int(str((CONSOLE_WIDTH - len(TITLE))//2)))
    print(" "*(int(CONSOLE_WIDTH*2-len(THANKS_TO)-3)), end="")
    print(THANKS_TO)
    print("~" * CONSOLE_WIDTH)
    print("")

class PDFMerger:

    def __init__(self) -> None:
        self.pdfs = list()
        self.merger = PdfFileMerger()

    def show_available_pdfs(self) -> bool:
        self.available_pdfs = dict()
        i = 1
        for f in os.listdir():
            if f.endswith(".pdf"):
                print("\t" + str(i) + ". " + f)
                self.available_pdfs[str(i)] = f
                i += 1

        if not self.available_pdfs.keys():
            print("[*] There are no PDFs in the current folder.")
            return False

        return True

    def get_pdfs(self, indexes: list):
        self.pdfs = [self.available_pdfs[i] for i in indexes]

    def merge(self) -> None:
        for pdf in self.pdfs:
            self.merger.append(open(pdf, 'rb'))

        with open("result.pdf", "wb") as fout:
            self.merger.write(fout)

def main():
    clear()

    show_introduction()

    P = PDFMerger()
    there_are_pdfs = P.show_available_pdfs()

    if there_are_pdfs:
        selected_str = input("PDFs: ")
        selected = selected_str.split(" ")    
        P.get_pdfs(selected)
        P.merge()

    print("")
    
if __name__ == "__main__":
    main()