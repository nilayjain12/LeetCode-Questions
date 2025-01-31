class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        total_count = 0

        T_grid = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

        for list_item in grid:
            if list_item in T_grid:
                count = T_grid.count(list_item)
                total_count += count
        
        return total_count
                    