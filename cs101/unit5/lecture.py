import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    elapsed = time.clock() - start
    return result, elapsed

def make_big_index(size):
    index = []
    letters = ('a' * 8).split()
    while len(index) < size:
        word = make_string(letters)
        add_to_index(index, word, 'fake')
        for i in range(len(letters) - 1, 0, -1):
            if letters[i] < 'z':
                letters[i] = chr(ord(letters[i]) + 1)
                break
            else:
                letters[i] = 'a'

def make_string(p):
    s = ""
    for e in p:
        s = s + e
    return s

def bad_hash_string(keyword, buckets):
    return ord(keyword[0]) % buckets

def hash_string(keyword, buckets):
    return sum([ord(c) % buckets for c in keyword]) % buckets

def test_hash_function(func, keys, size):
    results = [0] * size
    keys_used = []
    for w in keys:
        if w not in keys_used:
            hv = func(w, size)
            results[hv] = results[hv] + 1
            keys_used.append(w)
    return results

def make_hash_table(buckets):
    return [[] for _ in range(buckets)]

def get_bucket(htable, keyword):
    return htable[hash_string(keyword, len(htable))]