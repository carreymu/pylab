# O(nlog(n) + mlog(m)) time | O(1) space
def smallestDifference(arrayA, arrayB):
  arrayA.sort()
  arrayB.sort()
  print(f'arrayA:{arrayA}, arrayB:{arrayB}')
  left, right = 0, 0
  minVal = float("inf")
  currVal = float("inf")
  minPair = []
  while left < len(arrayA) and right < len(arrayB):
    leftVal = arrayA[left]
    rightVal = arrayB[right]
    if leftVal == rightVal:
      return [leftVal, rightVal]
    elif leftVal < rightVal:
      left += 1
      currVal = rightVal - leftVal
      print(f'currVal: {currVal}, leftVal:{leftVal}, rightVal:{rightVal}')
    else:
      right += 1
      currVal = leftVal - rightVal
      print(f'currSum: {currVal}, leftVal:{leftVal}, rightVal:{rightVal}')
    if minVal > currVal:
      minVal = currVal
      minPair = [leftVal, rightVal]
      print(f'minPair {minPair}')
  return minPair
if __name__ == "__main__":
    arrayA = [-1, 5, 10, 20, 28, 3]
    arrayB = [26, 134, 135, 15, 17]
    result = smallestDifference(arrayA, arrayB)
    print(f'result:{result}')
