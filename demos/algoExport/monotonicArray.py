def monotonicArray(array):
  isNonDecreasing = True
  isNonIncreasing = True
  for i in range(1, len(array)):
    direction = array[i] - array[i-1]
    if direction < 0:
      isNonDecreasing = False
    if direction > 0:
      isNonIncreasing = False
  return isNonDecreasing or isNonIncreasing

if __name__ == "__main__":
    array = [-1, -2, -4, 5, 10]
    result = monotonicArray(array)
    print(f"Is array monotonic? {result}")

