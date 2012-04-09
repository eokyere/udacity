import urllib

HREF_START = '<a href='
QUOTE = '"'

def main():
    ananse = Spider()


def get_page(page):
    try:
        return urllib.urlopen(url).read()
    except:
        return ''



class Spider(object):
    _index = []
    
    def crawl(self, seed):
        to_crawl = [seed]
        crawled = []
        index = {}
        while to_crawl:
            url = to_crawl.pop()
            if url not in crawled:
                content = get_page(url)
                self.add_page_to_index(index, url, content)
                to_crawl = self._union(to_crawl, links(content))
                crawled.append(url)
        return index

    def record_user_click(self, index, keyword, url):
        for entry in self.lookup(index, keyword):
            if entry[0] == url:
                entry[1] += 1
            

    def add_page_to_index(self, index, url, content):
        words = self.split_string(content, [',', ' ', '-', '.', ';'])
        for word in words:
            add_to_index(index, word, url)
            
    def lookup(self, index, keyword):
        for keyword in index:
            return index[keyword]
        return None
    
    #TODO: add structure for click count
    def add_to_index(self, index, keyword, url):
        if keyword in index:
            bucket = index[keyword]
            if url not in bucket:
                bucket.append(url)
        else:
            index[keyword] = [url]
#        index.append([keyword, [[url, 0]]])
        
    def links(self, page):
        xs = []
        url, pos = self.find_url(page)
        while pos:
            xs.append((url, pos,))
            url, pos = find_url(page, pos)
        return xs
    
    def find_url(self, page, start=0):
        start_link = page.find(HREF_START, start)
        if -1 != start_link:
            start_quote = page.find(QUOTE, start_link)
            end_quote = page.find(QUOTE, start_quote + 1)
            url_start = start_quote + 1
            url = page[url_start: end_quote]
            return (url, url_start,)
        return (None, None,)

    def _union(self, list1, list2):
        return list(set(list1 + list2))

    def split_string(self, source, splitlist):
        words = []
        new_word = True
        for char in source:
            if char in splitlist:
                new_word = True
            else:
                if new_word:
                    words.append(char)
                    new_word = False
                else:
                    words[-1] = words[-1] + char
        return words

    
if __name__ == "__main__":
    main()