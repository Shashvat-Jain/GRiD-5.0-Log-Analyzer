import fitz  

class PDFParser:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def remove_special_characters(self, text):
        special_characters = "!@#$%^&*()_+{}[]|\;:'\",.<>?`~-=\\/1234567890"
        cleaned_text = ''.join([char if char not in special_characters else ' ' for char in text])
        return cleaned_text

    def parse_pdf_to_text(self):
        try:
            pdf_document = fitz.open(self.pdf_path)
            text = ""

            for page_number in range(pdf_document.page_count):
                page = pdf_document.load_page(page_number)
                text += page.get_text("text")

            pdf_document.close()
            cleaned_text = self.remove_special_characters(text)
            return cleaned_text
        except Exception as e:
            return f"Error occurred: {e}"

    def save_cleaned_text_to_file(self, output_path):
        cleaned_text = self.parse_pdf_to_text()
        try:
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(cleaned_text)
            return f"Cleaned text saved to {output_path}"
        except Exception as e:
            return f"An error occurred while saving the cleaned text: {e}"
