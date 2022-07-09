"""
Author : @ Arun Singh | Date: Jul 5, 2022
time complexity: O(n) ~ |Vertex+Edges| = O(n)
space complexity: O(n)

if using stack then iterative , if using Queue then recursion in BFS approaches

"""

import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = collections.deque()
        time, fresh = 0, 0
        
        
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                # checking fresh oranges
                if grid[r][c] == 1:
                    fresh += 1
                # identifying all rotten oranges to use them in a queue, q
                if grid[r][c] == 2:
                    q.append((r,c))
        
        ## checking while q is empty and fresh is greater than Zero
        
        
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            
            #looping through queue. for storing rotten oranges count
            for i in range(len(q)):
                r, c = q.popleft()
                #traverse in all direction
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    
                    # if in bounds and fresh , make them rotten
                    if (row < 0 or row == len(grid) or
                       col < 0 or col ==len(grid[0]) or 
                       grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1


print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))