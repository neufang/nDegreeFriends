import sys
from collections import defaultdict
current_user = None
connection_dict = dict()

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    #print out N-degree friend (in the example case N=1)

    # parse the input we got from mapper.py
    user, friend,degree = line.split('\t')
    degree = int(degree)
    #get number of degree 

    print line
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    # two users if they share a identical friend are paired up, so they are considered as (N+1)-degree friends 
    if current_user == user:

        for people in connection_dict:
            # set the degree of new pair of N-degree friends (n_i, n_j)
            # Degree(n_i,n_j)= Degree(n_i, user) + Degree(user, n_j)
            updated_degree = degree + connection_dict[people]

            print "%s\t%s\t%d" %(friend, people,updated_degree )
            print "%s\t%s\t%d" %(people,friend,updated_degree )

    else:
        current_user = user
        connection_dict.clear()

    connection_dict[friend]=degree
