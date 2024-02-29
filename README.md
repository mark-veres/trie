
# Trie Implementation
A trie is an abstract datastructure, also know as a prefix tree. [See wikipedia](https://www.wikipedia.org/wiki/Trie)

#### Example:
```py
from trie import Trie

# create trie
trie = Trie()

# insert word in Trie
trie.insert("word")

# find specific word
trie.find("missing")

# find words that start with a prefix
matches = trie.startWith("w")
```

#### Working with word lists
Let's say you have a wordlist, that you want to insert into your trie.
```py
# dictionary.txt
abandon
abandonable
abandoned
abandonedly
abandonee
abandoner
abandoners
abandoning
abandonment
abandonments
abandons
abandum
abanet
abanga
abanic
abannition
```

```py
# main.py
from trie import Trie
trie = Trie()
words = open("./dictionary.txt").readlines()

for word in words:
	trie.insert(words.strip())
```