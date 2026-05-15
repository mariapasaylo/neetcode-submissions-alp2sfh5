class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #input grid  1 = land and 0 = water
        #output number of islands

        #graph traversal DFS
        #follow the path with ones
        #if continuous path then still on same island
        #if not find the next 1 that has not been visited
        #mark visited 1s as 0s because they belong to the same group
        islands = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):
            #return nothing if out of bounds and current node is 0
            if (r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c] == "0"):
                return

            #mark node as visited
            grid[r][c] = "0"
            #dfs through different directions
            for dh, dv in directions:
                dfs(r+dh, c+dv)

        #iterate through rows and cols
        for r in range(ROWS):
            for c in range(COLS):
                #if current node is 1 then dfs and increment islands
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        
        return islands
