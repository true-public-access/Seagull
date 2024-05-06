''' Seagull format this file defines the funtions that cleans/formats the data form the internet, 
    Copyright (C) 2024 Kai Broadbent 'BlazarKnight'

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to appblazarknight@gmail.com
'''
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