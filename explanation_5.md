Have to implement a Trie, a tree like structure that stores a dynamic set of strings.
First, made a class for TrieNode which has insert & suffixes methods.
Trie class is made with the insert word & find methods.

Complexities of this data structure:

TrieNode:

Insert a character:
Time complexity - O(1)
Space complexity - O(1)

suffixes of a node:
Time complexity: O(m^n)
Space complexity: O(m^n)
where m is maximum number of elements one level can have & n is the number of levels.

Trie:

Insert a word:
Time complexity: O(n)
Space complexity: O(n)

Find a prefix:
Time complexity: O(n)
Space complexity: O(1)
