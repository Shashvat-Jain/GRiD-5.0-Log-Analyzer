
def extractTextFromPdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text")
    return text


def preprocessText(text):
    text = re.sub(r'\s+', ' ', text)
    text = text.encode("ascii", "ignore").decode()
    return text


if (__name__ == "__main__"):
    pdf_path = "C:\\Users\\User\\Desktop\\NLP\\NLP_Project\\Application\\data\\pdf\\sample.pdf"
    print(extractTextFromPdf(pdf_path))
