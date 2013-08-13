cat $1 | python friends_mapper.py | sort -k1,1 | python friends_linker.py | sort -k1,1 |python friends_linker.py | sort -k1,1
