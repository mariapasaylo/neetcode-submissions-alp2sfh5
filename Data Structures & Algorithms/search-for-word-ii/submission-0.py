 #2d grid characters
        #a list of strings
        #return words present in a grid

        #use trie insert words with indices
        #dfs 
        #traverse grid once
        #for each character
        #   if c not in Trie
        #       end the search
        #   if end of word
        #       append word to results

 
 
 #create TrieNode class
        #   constructor func
        #       dictionary to store child nodes
        #       boolean to mark end of word

        #   insert func
        #       set cur node to self
        #       for each character in word
        #           if char not in dictionary
        #               add new Trienode
        #           #proceed to next node in dict
        #        mark isEnd = True because we reach the end of the word
class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.isEnd = True
                   
class Solution:


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #instantiate trie
        #for each word
            #add word to tree
        root = Trie()

        for w in words:
            root.insert(w)
        
        #store len of rows and columns
        #create set for result and visited nodes
        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        #helper dfs (row, col, node, word):
            #if out of bounds of the row/col or visited or current tile not in node children
                #return nothing
            #add (r,c) to visited
            #assign node to next node(next letter in board)
            #add letter to word
            #if node is the end of word
                #add word to results
            
            #recursive call right, left, up and down
            #remove (r,c) from visited
        def dfs(r,c,node,word):
            if r < 0 or r>=ROWS or c < 0 or c>=COLS or (r,c) in visited or board[r][c] not in node.children:
                return
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isEnd:
                res.add(word)
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r,c))
        
        #iterate through rows
            #iterate through columns
                #call dfs(r,c,root, "")
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")

        #return results as list
        return list(res)

