from urllib.request import urlopen
url="https://sites.google.com/view/classroom-workspace/" 
page=urlopen(url)
html_bytes=page.read()
html_string=html_bytes.decode("utf-8")
# print(html_string)
title_index=html_string.find("<title>")
print(title_index)
starting_index=title_index+len("<title>")
print(starting_index)
ending_index=html_string.find("</title>")
print(ending_index)
title=html_string[starting_index:ending_index]
print(title)
