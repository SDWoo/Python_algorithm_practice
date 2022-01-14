class Solution:
    grid: List[List[str]]  # class member 변수
    n_row: int
    n_col: int

    def dfs(self, i, j):
        if i < 0 or i >= self.n_row or j < 0 or j >= self.n_col or self.grid[i][j] == '0':
            return

        self.grid[i][j] = '0'
        self.dfs(i-1, j)  # down
        self.dfs(i+1, j)  # up
        self.dfs(i, j-1)  # left
        self.dfs(i, j+1)  # right

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.n_row, self.n_col = len(grid), len(grid[0])
        n_island = 0
        for i in range(self.n_row):
            for j in range(self.n_col):
                if grid[i][j] == '1':
                    self.dfs(i, j)
                    n_island += 1
        return n_island