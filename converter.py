import io

import ebooklib
import fitz  # PyMuPDF
from ebooklib import epub
from weasyprint import HTML


def convert_epub_to_pdf(epub_path, pdf_path):
    """ Convert an EPUB file to PDF. """
    book = epub.read_epub(epub_path)
    # Create a new PDF to store the final merged result
    final_pdf = fitz.open()

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            # Render HTML content to a PDF
            html_content = item.get_body_content().decode('utf-8')
            html = HTML(string=html_content)
            temp_pdf = html.write_pdf()

            # Open the temporary PDF and append it to the final PDF
            temp_pdf_doc = fitz.open(stream=io.BytesIO(temp_pdf), filetype="pdf")
            final_pdf.insert_pdf(temp_pdf_doc)

            temp_pdf_doc.close()

    final_pdf.save(pdf_path)
    final_pdf.close()
