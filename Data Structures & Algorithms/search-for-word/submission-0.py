class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #input is 2d grid
        #output true if the word exists

        #can only move left right up and down
        #dfs to traverse grid
        #use a set to keep track of cells we already visited

        #set to store visited tiles

        #dfs(r,c,i)
            #base case 
            # if i == len(word) this means that we have found the word in the grid
                #return True
            #if over bounds of the board or tile has been visited or current tile not a letter in word
                #return False
          #add r,c to visited
            #increment i
            #store following in isFound
            #dfs to right or
            #dfs to left or
            #dfs up or
            #dfs down
            #remove r,c to back track
            #return isFound
        
        #iterate through rows and columns
            #if dfs(r,c,0):
                #return True   
        #return False
        
        visited = set()
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r,c,i):
            if i == len(word):
                return True

            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visited or board[r][c] != word[i]:
                return False

            visited.add((r,c))
            i += 1
            
            isFound = dfs(r+1,c,i) or  dfs(r-1,c,i) or dfs(r,c+1,i) or dfs(r,c-1,i) 
            visited.remove((r,c))
            return isFound
    

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True

        return False





