def get_fileexturl(url):
    '''from urllib.parse import urlparse
    import os 
    path = urlparse(url).path
    path_without_params, _ = os.path.splitext(path.split('?')[0])
    _, file_extension = os.path.splitext(path_without_params)
    return file_extension'''
    import re
    match = re.search(r'\.([a-zA-Z0-9]+)$', url)
    if match:
        return match.group(1)
    else:
        return None
    
def clean(input:str,extent:str):








if __name__ == "__main__":
    
    print(clean("div>   <p>       Some text       <span>more text</span>       even more text   </p>   <ul>       <li>list item</li>       <li>yet another list item</li></ul></div><p>Some other text</p><ul>    <li>list item</li><li>yet another list item</li></ul>"))