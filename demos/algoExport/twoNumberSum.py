# O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
  for i in range(len(array) -1):
    firstNum = array[i]
    for j in range(i+1, len(array)):
      secondNum = array[j]
      if firstNum + secondNum == targetSum:
        return [firstNum, secondNum]
  return []

# O(n) time |O(n) space
def twoNumberSumSec(array, targetSum):
  ll = []
  for num in array:
    potentialMatch = targetSum - num
    if potentialMatch in ll:
      return [potentialMatch, num]
    else:
      ll.append(num)
  return []
# O(nlog(n)) time | O(1) space
def twoNumberSumTrd(array, targetSum):
  array.sort()
  leftPoint = 0
  rightPoint = len(array) -1
  while leftPoint < rightPoint:
    currentSum = array[leftPoint] + array[rightPoint]
    if currentSum< targetSum:
      leftPoint += 1
    elif currentSum > targetSum:
      rightPoint -= 1
    else:
      return [array[leftPoint], array[rightPoint]]
  return []


if __name__ == "__main__":
  array = [11, -4, 1, 6, 7 ,9, 8, -5]
  targetSum = 13
  #result = twoNumberSumSec(array, targetSum)
  result3 = twoNumberSumTrd(array, targetSum)
  print(result3)