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
    pgcont = len(reader.pages)
    pdfasstr = ''
    for i in range(0,pgcont):
        page = reader.pages[i]
        extracted_text = page.extract_text()
        pdfasstr = pdfasstr + extracted_text
    return pdfasstr

def clean(inp:str,extent:str):

    return can_opener_pdf(inp)


    








if __name__ == "__main__":
    
    print(clean('/home/supercow/PycharmProjects/Seagull/browser/2024GameManual.pdf','pdf'))