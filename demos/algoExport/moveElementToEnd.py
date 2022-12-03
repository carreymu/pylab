def moveElememtToEnd(array, toMove):
  i, j = 0, len(array) - 1
  while i < j :
    if array[i] == toMove and toMove == array[j]:
      i += 1
      j -= 1
    elif array[i] == toMove and toMove != array[j] :
      array[i], array[j] = array[j], array[i]
      i += 1
      j -= 1
    elif array[i] != toMove and toMove == array[j]:
      j -= 1
    elif array[i] != toMove and toMove != array[j]:
      i += 1
    else:
      pass
  return array

def moveElememtToEndNew(array, toMove):
  i, j = 0, len(array) - 1
  while i < j :
    if array[i] == toMove:
      array[i], array[j] = array[j], array[i]
      i += 1
      j -= 1
    elif array[i] != toMove:
      if toMove == array[j]:
        j -= 1
      else:
        i += 1  
    else:
      pass
  return array

# O(n) time | O(1) space
def moveElememtToEndOptimize(array, toMove):
  i, j = 0, len(array) - 1
  while i < j:
    # i < j is very import at last swap
    while i < j and toMove == array[j]:
      j -= 1
    if array[i] == toMove:
      array[i], array[j] = array[j], array[i] 
    print(f'i:{i}, j:{j}, arr - {array}')
    i += 1
  return array
if __name__ == "__main__":
    #array = [2, 1, 3, 2, 3, 2, 4, 2]
    array = [2,1,2,2,2,3,4,2]
    toMove = 2
    result = moveElememtToEndOptimize(array, toMove)
    print(result)