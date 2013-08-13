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
`python uniq.py | python friends_reducer.py  $N`

For large **N**, multiple run of friends_linker.py is needed.

Attention
-------
Follow the idea of hadoop streaming

`toy solution, no function, no opp`

Complexity Analysis
------

- `friends_mapper.py` is simple, for each pair of friends, print two orders of them, such as `mick ziggy` **or** `ziggy mick`.
  Given M as the number of line in the input file, The time complexity is M, the space complexity is 2M.

- `friends_linker.py` 

    - Best case: each user only has one friend, and no common friend. So no N-degree friend (N>1) can be found.
    The time complexity is M, the space complexity is M.

    - Worse case: all users are fully connected. line 23-29 run O(M^2) time. So the time complexity is O(M^2), 
    the space complexity is O(M^2).

    - Average case: Let average number of friends of a user is K,  line 23-29 run O(K^2). 
    So the time complexity is O(K^2*M/K ) ~= O(MK).

- `friends_reducer.py`: its complexity is linear to the number of line of its input.


Discussion
------
The initition of the methods: 
- *Transitive Relation*: Given a user A, if B is a n-degree friend of A, C is a m-degree friend of A, then B and C are (m+n)-degree friends,
mutually.
- *Shortest Path*: If there exists several paths of connecting user B and C, the min path is chosen as the final friend-degree between them.

Following those ideas, initially `friends_mapper.py` emit all friend pairs and the degrees ( =1 as they are directly connected).

```
davidbowie      omid    1
omid    davidbowie      1
davidbowie      kim     1
kim     davidbowie      1
kim     torsten 1
torsten kim     1
...
```

After sorting on the first column,
```
davidbowie      omid    1
omid    davidbowie      1
davidbowie      kim     1
kim     davidbowie      1
kim     torsten 1
torsten kim     1
torsten omid    1
....
```
We can see the friends of one user are aggregated. Then following the *Transitive Relation*, we can build pairs
of friends in any degree with `friends_linker.py`.

`friends_linker.py` also keep the original record from input. After running 

`cat input_file | python friends_mapper.py | sort -k1,1 | python friends_linker.py | sort -k1,1`

we get following results,

```
brendan kim     2
brendan omid    2
brendan torsten 1
davidbowie      kim     1
davidbowie      mick    2
davidbowie      omid    1
davidbowie      torsten 2
davidbowie      torsten 2
```

Notice the duplcate pairs of `davidbowie  torsten`, as they have mutually friends `kim` and `omid`. 
Those identical pairs shall be removed to save running time of following steps.

One more run of `python friends_linker.py` produce friends with degree <= 4. ( **n runs of `friends_linker.py` generate
degree of 2^n at most.**)

In the result we notice that

```
brendan kim     2
brendan kim     2
brendan kim     4
brendan kim     4
```

Following the rule of *Shortest Path*, only the shortest path 2 between `brendan` and  `kim` is kept. 

Therefore, `uniq.py` is introduced to merge duplicate pair and keep the first record of a unique pair, which
has the smallest degree after sorting.


The following scripts of caculating friends of degree 3 can simply evaluate the contribution of `uniq.py`. The results give
the overall number of friend pairs.

`source drg3.sh input_file | wc -l` 

`source drg3_uniq.sh input_file | wc -l`

Using the example input file, they generate **148** and **40** friend pairs seperately. `uniq.py` makes the procedure more efficiently, as 
redundant updating degrees of friends can be avoided. The improvement is epecially significant for mutiple calcuation and big data.

Eventually `friends_reducer.py` filters the degree bigger than **N** and formats the output as required.

Regarding [Six degrees of separation](http://en.wikipedia.org/wiki/Six_degrees_of_separation), intensive
running of the friend-matching is not necessary.

Given **N**, the time of running `friends_linker.py` is *ceiling(sqrt(N))*.

