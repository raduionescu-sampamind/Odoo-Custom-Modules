import re

d_file = open('diana_codes.txt', 'rt')
for d in d_file:
    d = d.rstrip()
    o_file = open('other_codes.txt', 'rt')
    for o in o_file:
        o = o.strip()
        if d == o:
            print(d + ' = ' + o)
            break
