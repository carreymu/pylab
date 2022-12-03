# O(n) time | O(n) space
def spiralTraverse(array):
  result = []
  spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
  return result
def spiralFill(array, startRow, endRow, startCol, endCol, result):
  if startRow > endRow or startCol > endCol:
    return
  for col in range(startCol, endCol + 1):
    result.append(array[startCol][col])

  for row in range(startRow + 1, endRow + 1):
    result.append(array[row][endCol])

  for col in reversed(range(startCol,endCol)):
    result.append(array[endRow][col])

  for row in reversed(range(startRow + 1, endRow)):
    result.append(array[row][startCol])

  spiralFill(array, startRow + 1, endCol - 1, startCol + 1, endCol - 1, result)

if __name__ == "__main__":
  array = []
  array.append([1, 2, 3, 4])
  array.append([12, 13, 14, 5])
  array.append([11, 16, 15, 6])
  array.append([10, 9, 8, 7])
  
  result = spiralTraverse(array)
  print(f"read spiral array to one line, result: ${result}")