# Read Log file in python
from module.typeChange import typeCheck, pdfToText, csvToText, pdfToCsv, textToCsv


def readCompFile(log_path):
    comp_files = ""
    if typeCheck:
        if typeCheck(log_path) == 'pdf':
            compFiles = pdfToText(log_path)
        elif typeCheck(log_path) == 'csv':
            compFiles = csvToText(log_path)
        else:
            return False
    return comp_file


if __name__ == "__main__":
    print(readCompFile("../testComp/test.pdf"))
