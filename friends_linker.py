import sys

current_user = None
connection_set = set()

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    #print out N-degree friend (in the example case N=1)
    print line

    # parse the input we got from mapper.py
    user, friend = line.split('\t', 1)
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    # two users if they share a identical friend are paired up, so they are considered as (N+1)-degree friends 
    if current_user == user:

        for people in connection_set:
            print "%s\t%s" %(friend, people)
            print "%s\t%s" %(people,friend)

    else:
        current_user = user
        connection_set.clear()

    connection_set.add(friend)