# Define a procedure, udacify, that takes as 
# input a string, and returns a string that 
# is an uppercase 'U' followed by the input string.
# for example, when we enter

# print udacify('dacians')

# the output should be the string 'Udacians'

# Make sure your procedure has a return statement.

def udacify(s):
    return 'U' + s

# Define a procedure, median, that takes three
# numbers as its inputs, and outputs the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b
        
def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def smaller(a, b):
    return a if a < b else b

def median(a, b, c):
    # easy solution for this will be return sorted([a,b,c])[1]
    return bigger(a, smaller(b, c)) if a < b else smaller(a, bigger(b, c))


def looper(n):
    steps = 0
    while n != 1:
        if n % 2 == 0: # n is even
            n = n/2
        else:
            n = 3*n + 1    
        steps += 1
    return steps

if __name__ == "__main__":
#    for i in range(1, 10000000):
        i = 1000000342498327401927489132749213011111111009993242423421
        print '>>>> looper for: ', i, looper(i)