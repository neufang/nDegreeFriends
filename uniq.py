import sys
"""
omit duplicate results of calculating degrees
"""
# input comes from STDIN
curr_pair = None
for line in sys.stdin:
    line = line.strip()

    user,friend,degree = line.split()
    pair = "\t".join([user,friend])
    if curr_pair != pair:
        curr_pair = pair
        print line
