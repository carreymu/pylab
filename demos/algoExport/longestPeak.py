def longestPeak(array):
  """
  find longest peek
  """
  longestPeakLength = 0
  # result = []
  i = 1
  while i < len(array) -1:
    isPeak = array[i] > array[i - 1] and array[i+1] < array[i]
    print(f"i={i}, is {array[i]} > {array[i-1]} and {array[i]} > {array[i+1]} ? {isPeak}")
    if not isPeak:
      i += 1
      continue
    
    leftIdx = i - 2
    while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
      leftIdx -= 1
      print(f"left while: i = {i}, leftIdx {leftIdx}")

    rightIdx = i + 2
    while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
      rightIdx += 1
      print(f"right while:  i = {i}, rightIdx {rightIdx}")
    print("*" * 10)
    currentPeakLength = rightIdx - leftIdx - 1
    longestPeakLength = max(longestPeakLength, currentPeakLength)

    print(f"1. current k:{i}-v:{array[i]}, left k:{leftIdx}-v:{array[leftIdx]}, right k:{rightIdx}-v:{array[rightIdx]}, currentPeak {currentPeakLength}, longestPeak {longestPeakLength}")
    i = rightIdx
    print(f"1. current k:{i}-v:{array[i]}, left k:{leftIdx}-v:{array[leftIdx]}, right k:{rightIdx}-v:{array[rightIdx]}, currentPeak {currentPeakLength}, longestPeak {longestPeakLength}")
    print(f"peak left: {leftIdx}, right:{rightIdx}, currentPeakLength:{currentPeakLength}, longestPeakLength:{longestPeakLength}")
    print(array[slice(leftIdx+1, rightIdx)])
  return longestPeakLength

if __name__ == "__main__":
    array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, 1,-3, -5, 2, 3]
    result = longestPeak(array)
    print(f"longest peek result: {result}")