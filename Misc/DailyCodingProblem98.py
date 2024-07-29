"""
Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
"""

class solution():
    def exists(board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if solution.dfs(board, word, 0, i, j):
                        return True
                    
        return False

    def dfs(board, word, wordIdx, i, j):
        # check if have found whole word
        if wordIdx == len(word):
            return True
        # check if indices are valid, and letter matches the next letter of the word
        if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[wordIdx]):
            return False
        
        # mark cell as seen
        cur = board[i][j]
        board[i][j] = '0'

        # conduct dfs: is true if one of the searches was successful, otherwise false
        check = (solution.dfs(board, word, wordIdx+1, i-1, j) or
                solution.dfs(board, word, wordIdx+1, i+1, j) or
                solution.dfs(board, word, wordIdx+1, i, j-1) or
                solution.dfs(board, word, wordIdx+1, i, j+1))
        
        # revert cell
        board[i][j] = cur

        return check
        

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(solution.exists(board, "ABCCED"))
print(solution.exists(board, "SEE"))
print(solution.exists(board, "ABCB"))