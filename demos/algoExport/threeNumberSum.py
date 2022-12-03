# O(n^2) time | O(n) space
def threeNumberSumWhile(array, targetSum):
  results = []
  currentNum = 0
  left = 0
  array.sort()
  print(f"sorted array:{array}")
  for i in range(len(array) - 2):
    currentNum = array[i]
    left = i + 1
    right = len(array) - 1
    #print(f"i={i}")
    while left < right:
      #print(f"left:{left},right:{right}")
      tmpSum = array[left] + array[right] + currentNum
      if tmpSum == targetSum:
        results.append([array[i], array[left] ,array[right]])
        print([i, left ,right])
        left += 1
        right -= 1
      elif tmpSum < targetSum:
        left += 1
      else:
        right -= 1
  return results
if __name__ == "__main__":
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    targetSum = 0
    results = threeNumberSumWhile(array, targetSum)
    print(results)

