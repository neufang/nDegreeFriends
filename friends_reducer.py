import sys

#global variable to control the degree of friends
try:
    N= int(sys.argv[1])
except:
    N=2

current_user = None
current_set = set()
word = None

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()

    # parse the input we got from linker.py
    user, friend,degree = line.split()
    degree = int(degree)

    if current_user == user:
        #add new friend to the current friend-set
        if degree<=N:
            current_set.add(friend)
    else:
        if current_user:
            # write list of friends to STDOUT
            print '%s\t%s' % (current_user, "\t".join(sorted(current_set)))
        current_set.clear()
        if degree <=N:
            current_set.add(friend)
        current_user = user

# do not forget to output the last word if needed!
if current_user == user:
    print '%s\t%s' % (current_user, "\t".join(sorted(current_set)))
