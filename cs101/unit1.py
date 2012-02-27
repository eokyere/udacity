def main():
    page = """<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Udacity</title>
</head>

<body>
<h1>Udacity</h1>

<p><b>Udacity</b> is a private institution of <a href="http://www.wikipedia.org/wiki/Higher_education">higher education founded by</a> <a href="http://www.wikipedia.org/wiki/Sebastian_Thrun">Sebastian Thrun</a>, David Stavens, and Mike Sokolsky with the goal to provide university-level education that is "both high quality and low cost".
It is the outgrowth of a free computer science class offered in 2011 through Stanford University. Currently, Udacity is working on its second course on building a search engine. Udacity was announced at the 2012 <a href="http://www.wikipedia.org/wiki/Digital_Life_Design">Digital Life Design</a> conference.</p>
</body>
</html>"""
    print links(page)

HREF_START = '<a href='
QUOTE = '"'

def links(page):
    xs = []
    url, pos = find_url(page)
    while pos:
        xs.append((url, pos,))
        url, pos = find_url(page, pos)
    return xs

def find_url(page, start=0):
    start_link = page.find(HREF_START, start)
    start_quote = page.find(QUOTE, start_link)
    end_quote = page.find(QUOTE, start_quote + 1)
    url_start = start_quote + 1
    url = page[url_start: end_quote]
    return (url, url_start,)

if __name__ == "__main__":
    main()