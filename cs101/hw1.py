from unit1 import links

def main():
    print 'Q1.'
    q1()
    print 'Q2. ', q2()
    print 'Q4. ', '%.4f' % q4() == '0.2998'
    print 'Q6. ', q6() == 'udacious'
    print 'Q7a. ', q7('hehehehohohoooo') == 10
    print 'Q7b. ', q7('heheh') == -1
    print 'Q8a. ', q8('zip files are zipped') == 14
    print 'Q8b. ', q8('zip files are compressed') == -1
    print 'Q8b. ', q8('zippperzi pzipzipzip') == 11
    print 'Q9a. ', q9(3.14159) == '3'
    print 'Q9b. ', q9(27.63) == '28'
    

def q1():
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
    xs = [x[0] for x in links(page)]
    for s in ['http://www.w3.org/1999/xhtml',
              'http://www.wikipedia.org/wiki/Higher_education',
              'http://www.wikipedia.org/wiki/Sebastian_Thrun',
              'both high quality and low cost',
              'http://www.wikipedia.org/wiki/Digital_Life_Design']:
        print '%s --> %s' % (s, 'Found' if s in xs else 'NOT Found')

def q2():
    """Print the number of hours in 7 wks"""
    hours_per_day = 24
    days_per_week = 7
    return 7 * days_per_week * hours_per_day
    

def q4(nano=1):
    """Distance in meters that light travels in one nanosecond."""
    speed_of_light = 299800000. # m/s
    nano_per_sec = 10. ** 9
    return speed_of_light/nano_per_sec

def q6():
    """Given s and t defined below, write code that prints out udacious."""
    s = 'udacity'
    t = 'bodacious'
    return s[0] + t[2:]

def q7(text):
    """Print out the first occurence of 'hoo' in text or -1 if not found"""
    return text.find('hoo')

def q8(text):
    """Print out the second occurence of 'zip' in text or -1 if not found."""
    s = 'zip'
    return text.find(s, text.find(s) + 1)

def q9(x):
    s = str(round(x))
    return s[:s.find('.')]

if __name__ == "__main__":
    main()