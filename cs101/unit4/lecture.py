def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            if url not in entry[1]:
                entry[1].append(url)
            return
    index.append([keyword, [url]])
    
def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []

def add_page_to_index(index, url, content):
    keywords = content.split()
    for keyword in keywords:
        add_to_index(index, keyword, url)
        

def crawl_web(seed):
        to_crawl = [seed]
        crawled = []
        index = []
        while to_crawl:
            url = to_crawl.pop()
            if url not in crawled:
                content = get_page(url)
                self.add_page_to_index(index, url, content)
                to_crawl = self._union(to_crawl, links(content))
                crawled.append(url)
        return index
