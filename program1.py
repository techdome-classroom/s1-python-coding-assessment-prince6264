class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r, c):
            # If out of bounds or the cell is water or already visited, return
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or grid[r][c] == 'W':
                return
            # Mark the cell as visited
            visited.add((r, c))
            # Visit all 4 possible directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left
        
        island_count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L' and (r, c) not in visited:
                    # Found an unvisited land cell, start DFS
                    dfs(r, c)
                    island_count += 1
        
        return island_count
