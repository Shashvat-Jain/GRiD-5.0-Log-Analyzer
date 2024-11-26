# Check the File Type
import PyPDF2


def typeCheck(file_name):
    if file.endswith('.txt'):
        return 'txt'
    elif file.endswith('.csv'):
        return 'csv'
    elif file.endswith('.pdf'):
        return 'pdf'
    else:
        return False


def pdfToText(file):
    pdfFileObj = open(file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    text = ""
    for i in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(i)
        text += pageObj.extractText()
    return text


def csvToText(file):
    with open(file, "r") as f:
        text = f.read()
    return text


def pdfToCsv(file):
    pdfFileObj = open(file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    text = ""
    for i in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(i)
        text += pageObj.extractText()
    return text


def textToCsv(file):
    with open(file, "r") as f:
        text = f.read()
    return text


if __name__ == "__main__":
    print(typeCheck("../testComp/test.pdf"))
    print(pdfToText("../testComp/test.pdf"))
    print(csvToText("../testComp/test.csv"))
    print(pdfToCsv("../testComp/test.pdf"))
    print(textToCsv("../testComp/test.txt"))
