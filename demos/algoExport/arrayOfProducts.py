# O(n^2) time | O(n) space
def arrayOfProducts(array):
  products = [1 for _ in range(len(array))]
  for i in range(len(array)):
    runningProduct = 1
    for j in range(len(array)):
      if i != j:
        runningProduct *= array[j]
    products = runningProduct
  return products

def arrayOfProductsOpt(array):
  products = [1 for _ in range(len(array))]
  leftProducts = [1 for _ in range(len(array))]
  rightProducts = [1 for _ in range(len(array))]

  leftRunningProduct = 1
  for i in range(len(array)):
    leftProducts[i] = leftRunningProduct
    print(f"leftProducts[{i}]={leftProducts[i]}, leftRunningProduct = {leftRunningProduct}")
    leftRunningProduct *= array[i]
    print(f"array[{i}]={array[i]}, leftRunningProduct = {leftRunningProduct}")
    print('*' * 10)
  print('#' * 5)
  rightRunningProduct = 1
  for i in reversed(range(len(array))):
    rightProducts[i] = rightRunningProduct
    print(f"rightProducts[{i}]={rightProducts[i]}, rightRunningProduct = {rightRunningProduct}")
    rightRunningProduct *= array[i]
    print(f"array[{i}]={array[i]}, rightRunningProduct = {rightRunningProduct}")
    print('*' * 10)
  
  for i in range(len(array)):
    products[i] = leftProducts[i] * rightProducts[i]
  return products

if __name__ == "__main__":
  array = [5, 1, 4, 2]
  result = arrayOfProductsOpt(array)
  print(f'result is {result}')