nDegreeFriends
==============
Preliminary Solution to  SoundCloud Data Challenge

https://gist.github.com/omidaladini/42ab4f7d058984da9d0f

Given a set S of pairs of usernames corresponding to mutual friendships in a social network, 
write a program to output each user’s i-th degree friends

Execution
-------
**$N** is degree of friends

`cat input_file | python friends_mapper.py | sort -k1,1 | python friends_linker.py | sort -k1,1 |`
`uniq | python friends_reducer.py  $N`

For large **N**, multiple run of friends_linker.py is needed.

Attention
-------
Follow the idea of hadoop streaming

`toy solution, no function, no opp`

redundant updating of degree of friends can be avoided.


