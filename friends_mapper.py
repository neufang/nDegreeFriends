
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    connection = line.split()
    # increase counters
    user = connection[0]
    for friend in connection[1:]:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        # print all possilbe pairs of connected users, e.g. 'mick zippy', 'zippy mick'
        # tab-delimited
        print '%s\t%s\t1' % (user, friend)
        print '%s\t%s\t1' % (friend,user)
