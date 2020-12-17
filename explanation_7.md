Have to implement a HTTPRouter using a Trie.

First, initialized a RouteTrieNode, which has value, handler & reference to next node.
then utilized this node to implement RouteTrie.

RouteTrieNode:

Time Complexity - O(1)
Space Complexity - O(1)

RouteTrie:

Time Complexity - O(n)
Space Complexity - O(n) (lookup, add handler)
