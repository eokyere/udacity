from lecture import links

def main():
    print 'Q1.', q1()
    print 'Q2. ', q2()

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
    search = ['http://www.w3.org/1999/xhtml',
              'http://www.wikipedia.org/wiki/Higher_education',
              'http://www.wikipedia.org/wiki/Sebastian_Thrun',
              'both high quality and low cost',
              'http://www.wikipedia.org/wiki/Digital_Life_Design']
    return [(s, s in xs) for s in xs]

def q2():
    """Print the number of hours in 7 wks"""
    return hours_in_weeks(7)

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


def hours_in_weeks(weeks):
    hours_per_day = 24
    days_per_week = 7
    return weeks * days_per_week * hours_per_day

if __name__ == "__main__":
    main()