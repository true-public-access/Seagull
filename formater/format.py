


def clean(input:str):
    import html2text
    import codecs
#    from usr.lib.python3 import BeautifulSoup4
#    HtmlFile = codecs.open(input, 'r', encoding='latin-1')
#    text = BeautifulSoup4(HtmlFile.read()).text
    cleaned = html2text.html2text(input)
    return cleaned 

if __name__ == "__main__":
    
    print(clean("div>   <p>       Some text       <span>more text</span>       even more text   </p>   <ul>       <li>list item</li>       <li>yet another list item</li></ul></div><p>Some other text</p><ul>    <li>list item</li><li>yet another list item</li></ul>"))