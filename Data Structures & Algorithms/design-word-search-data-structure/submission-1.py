class Node:
    def __init__(self):
        self.vals = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        #use Trie data structure
        self.root = Node()

    def addWord(self, word: str) -> None:
        #insert letters into the trie
        curr = self.root
        for c in word:
            if c not in curr.vals:
                curr.vals[c] = Node() #make a new node
            curr = curr.vals[c] #proceed to next node
        curr.isEnd = True #we reached the end of the word
        

    def search(self, word: str) -> bool:
        #true if word is in word dictionary
        #"." means any letter
        # use dfs when c == "."
        #define dfs(j, root)
            #set cur to be root
            #iterate through j to length of word
                #store current letter
                #if c is "."
                    #iterate through each child value in dictionary NOTE: iterate through all characters
                        #if recursive call (i+1, child)
                            #return True
                        #return False
                #else:
                    #if c is not in the dictionary
                        #return False
                    #advance to next node
            #return cur.isEnd
        #return call dfs(0,root)
        def dfs(j, root):
            cur = root
            for i in range(j,len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.vals.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur.vals:
                        return False
                    cur = cur.vals[c]
            return cur.isEnd
        
        return dfs(0,self.root)
        
            
