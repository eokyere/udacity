#Procedures and If

#Define a procedure, unique, that takes three numbers as its inputs and returns
#the Boolean value True if all three numbers are different. Otherwise, it should
#return the Boolean value False.

def unique(a, b, c):
    return not (a == b or a == c or b == c)


#Prefix Removal


#Define a procedure, remove_prefix, that takes as input a string, and returns a
#string that is the part of the string following the first hyphen -. If the input string does
#not contain any hyphen -, remove_prefix should return the full input string.

def remove_prefix(s):
    if '-' in s:
        return s[s.index('-') + 1:]
    return s


#Collatz Returns!


#Define a procedure, collatz_steps, that takes as input a positive integer, n, and returns
#the number of steps it takes to reach 1 by following these steps:

#    If n is even, divide it by 2. (You can test for evenness using n % 2 == 0.)
#    If n is odd, replace it with 3n + 1.

def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3 * n + 1    
        steps += 1
    return steps
        

#List Explosion


#Define a procedure, explode_list, that takes as inputs a list and a number, n.
#It should return a list which contains each of the elements of the input list,
#in the original order, but repeated n times.

def explode_list(p, n):
#    more elegant
#    return reduce(lambda a, b: a + b, [[x] * n for x in p], [])
    xs = []
    for entry in p:
        xs += [entry for i in range(n)]
    return xs


#Reverse Index


#Define a procedure, reverse_index, that takes as input a Dictionary, and
#returns a new Dictionary where the keys are the values in the input dictionary.
#The value associated with a key in the result is a list of all the keys in the
#input dictionary that match this value (in any order).

def reverse_index(dict):
    d = {}
    for key in dict:
        value = dict[key]
        if value in d:
            d[value].append(key)
        else:
            d[value] = [key]
    return d


#Same Structure

#Define a procedure, same_structure, that takes two inputs. It should output
#True if the lists contain the same elements in the same structure, and False
#otherwise. Two values, p and q have the same structure if:

#    Neither p or q is a list.

#    Both p and q are lists, they have the same number of elements, and each
#    element of p has the same structure as the corresponding element of q.


#For this procedure, you can use the is_list(p) procedure from Homework 6:

def is_list(p):
    return isinstance(p, list)


def same_structure(a,b):
    if is_list(a) and is_list(b):
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if not same_structure(a[i], b[i]):
                return False
        return True
    return not (is_list(a) or is_list(b))



#Reachability

#Single Gold Star

#Define a procedure, reachable(graph, node), that takes as input a graph and a
#starting node, and returns a list of all the nodes in the graph that can be
#reached by following zero or more edges starting from node.  The input graph is
#represented as a Dictionary where each node in the graph is a key in the
#Dictionary, and the value associated with a key is a list of the nodes that the
#key node is connected to.  The nodes in the returned list may appear in any
#order, but should not contain any duplicates.


def reachable(graph, node):
    nodes = []
    followed = []
    unfollowed = [node]
    
    while unfollowed:
        node = unfollowed.pop()
        if node not in followed:
            followed.append(node)
            if node in graph:
                nodes.append(node)
                for node in graph[node]:
                    if node not in followed and node not in unfollowed:
                        unfollowed.append(node)
    return nodes





#Spelling Correction

#Double Gold Star

#For this question, your goal is to build a step towards a spelling corrector,
#similarly to the way Google used to respond,

#    "Did you mean: audacity"


#when you searched for "udacity" (but now considers "udacity" a real word!).

#One way to do spelling correction is to measure the edit distance between the
#entered word and other words in the dictionary.  Edit distance is a measure of
#the number of edits required to transform one word into another word.  An edit
#is either: (a) replacing one letter with a different letter, (b) removing a
#letter, or (c) inserting a letter.  The edit distance between two strings s and
#t, is the minimum number of edits needed to transform s into t.

#Define a procedure, edit_distance(s, t), that takes two strings as its inputs,
#and returns a number giving the edit distance between those strings.

#Note: it is okay if your edit_distance procedure is very expensive, and does
#not work on strings longer than the ones shown here.

#The built-in python function min() returns the mininum of all its arguments.

#print min(1,2,3)
#>>> 1

#def edit_distance(s,t):
#    m = len(s)
#    n = len(t)
#    
#    v = [[0 for col in range(n)]
#            for row in range(m)]
#    
#    for i in range(m):
#        v[i][0] = i
#    
#    for i in range(n):
#        v[0][i] = i
#    
#    for i in range(1, m):
#        for j in range(1, n):
#            if (s[i-1] == t[j-1]):
#                v[i][j] = v[i-1][j-1]
#            else: 
#                v[i][j] = 1 + min(v[i][j-1], v[i-1][j], v[i-1][j-1])
#    print
#    
#    for row in v:
#        print row
#    
#    
#    return v[m-1][n-1]

def edit_distance(s, t):
    def distance(s1, t1, i=0, j=0):
        if j == len(t1):
            return len(s1) - i
        if i == len(s1):
            return len(t1) - j     
        if (s1[i] == t1[j]): 
            return distance(s1, t1, i+1, j+1)
        if (s1[i] != t1[j]):
            return 1 + min(distance(s1, t1, i,   j+1), 
                           distance(s1, t1, i+1, j), 
                           distance(s1, t1, i+1, j+1))    
    return distance(s, t)


#Multi-word Queries

#Triple Gold Star

#For this question, your goal is to modify the search engine to be able to
#handle multi-word queries.  To do this, we need to make two main changes:

#    1. Modify the index to keep track of not only the URL, but the position
#    within that page where a word appears.

#    2. Make a version of the lookup procedure that takes a list of target
#    words, and only counts a URL as a match if it contains all of the target
#    words, adjacent to each other, in the order they are given in the input.

#For example, if the search input is "Monty Python", it should match a page that
#contains, "Monty Python is funny!", but should not match a page containing
#"Monty likes the Python programming language."  The words must appear in the
#same order, and the next word must start right after the end of the previous
#word.

#Modify the search engine code to support multi-word queries. Your modified code
#should define these two procedures:

#    crawl_web(seed) => index, graph
#        A modified version of crawl_web that produces an index that includes
#        positional information.  It is up to you to figure out how to represent
#        positions in your index and you can do this any way you want.  Whatever
#        index you produce is the one we will pass into your multi_lookup(index,
#        keyword) procedure.

#    multi_lookup(index, list of keywords) => list of URLs
#        A URL should be included in the output list, only if it contains all of
#        the keywords in the input list, next to each other.


def multi_lookup(index, query):
    urls = {}
    indexed = []
    
    for keyword in query:
        if keyword not in index:
            return None
        indexed.append(index[keyword])
    
    urls = indexed[0]
    for o in indexed[1:]:
        for url in o:
            if url not in urls:
                continue
            found = False
            positions = o[url]
            for position in positions:
                if position - 1 in urls[url]:
                    found = True
                    urls[url].append(position)
                    break
            if not found:
                del urls[url]
    
    return urls.keys()
    

def crawl_web(seed): # returns index, graph of inlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>, [list of pages it links to]
    index = {}  # <keyword>, [[url, position] ..]
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index, url, content):
    words = content.split()
    for position, word in enumerate(words):
        add_to_index(index, position, word, url)
        
def add_to_index(index, position, keyword, url):
    if keyword in index:
        o = index[keyword]
        if url in o:
            if position not in o[url]:
                o[url].append(position)
        else:
            o[url] = [position]
    else:
        if not is_tag(keyword):
            index[keyword] = {url: [position]}

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None
    
def is_tag(word):
    return word[0] == '<' and word[-1] == ">"


cache = {
   'http://www.udacity.com/cs101x/final/multi.html': """<html>
<body>

<a href="http://www.udacity.com/cs101x/final/a.html">A</a><br>
<a href="http://www.udacity.com/cs101x/final/b.html">B</a><br>

</body>
""", 
   'http://www.udacity.com/cs101x/final/b.html': """<html>
<body>

Monty likes the Python programming language
Thomas Jefferson founded the University of Virginia
When Mandela was in London, he visited Nelson's Column.

</body>
</html>
""", 
   'http://www.udacity.com/cs101x/final/a.html': """<html>
<body>

Monty Python is not about a programming language
Udacity was not founded by Thomas Jefferson
Nelson Mandela said "Education is the most powerful weapon which you can
use to change the world."
</body>
</html>
""", 
}

def get_page(url):
    if url in cache:
        return cache[url]
    else:
        print "Page not in cache: " + url
        return None
    







