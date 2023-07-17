def uniquePaths(m: int, n: int) -> int:
    # Create an m x n grid filled with zeros
    grid = [[0] * n for _ in range(m)]
    
    # Set the last row to have all elements as 1
    grid[-1] = [1] * n
    
    # Set the last column to have all elements as 1
    for row in grid:
        row[-1] = 1
    
    # Iterate through the grid from bottom-right to top-left
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            # If the current position is not already filled (0), calculate the number of unique paths
            if grid[i][j] == 0:
                # The number of unique paths to reach a position is the sum of paths from the next row (down) and the next column (right)
                grid[i][j] = grid[i+1][j] + grid[i][j+1]
    
    # Return the number of unique paths from the top-left corner to the bottom-right corner
    return grid[0][0]