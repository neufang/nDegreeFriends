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


Complexity Analysis
------

`friends_mapper.py` is simple, for each pair of friends, print two orders of them, such as  
`mick ziggy` **or** `ziggy mick`
Given M as the number of line in the input file, The time complexity is M, the space complexity is 2M.

`friends_linker.py` 

Best case: each user only has one friend, and no common friend. So no N-degree friend (N>1) can be found.
The time complexity is M, the space complexity is M.

Worse case: all users are fully connected. line 23-29 run O(M^2) time. So the time complexity is O(M^2), 
the space complexity is O(M^2).

Average case: Let average number of friends of a user is K,  line 23-29 run O(K^2). 
So the time complexity is O(K^2*M/K ) ~= O(MK).

`friends_reducer.py`: its complexity is linear to the line of its input.
