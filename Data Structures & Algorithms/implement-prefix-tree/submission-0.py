#create new class to define node
#a hashmap that stores references to child nodes
#boolean flag to indicate if it is the end of the word
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class PrefixTree:

    def __init__(self):
        #root has no characters
        self.root = TrieNode()
        
        

    def insert(self, word: str) -> None:
        '''inserts word into the prefix tree'''
        #start at root node
        #iterate through word
        #   if current node does not contain the curr letter
        #       create new node
        #   continue to next node
        #set isEnd to True
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        '''return true if word is in the prefix tree otherwise false'''
        #start at root node
        #iterate through word
        #   if word[i] not in node or if isEnd == false:
        #       return false
        #   continue to next node
        #return isEnd
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        '''return true if prefix already exists in trie otherwise false'''
        #can't use search because this looks for the whole word
        #same implementation as search but return true when we finish iteration of prefix
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

        
        