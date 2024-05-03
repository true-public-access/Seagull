def can_opener_pdf(file):
    from PyPDF2 import PdfReader

    reader = PdfReader(file)
    page = reader.pages[0]
    extracted_text = page.extract_text()
    return extracted_text


def clean(input:str,extent:str):

    return can_opener_pdf(input)


    








if __name__ == "__main__":
    
    print(clean('leggett_v._the_sanctuary_at_false_cape_condo._assn._order.pdf','pdf'))