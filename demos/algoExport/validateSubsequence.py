
def validateSubsequence(sequence, arr):
  arrIdx = 0
  seqIdx = 0
  while arrIdx < len(arr) and seqIdx < len(sequence):
    if arr[arrIdx] == sequence[seqIdx]:
      seqIdx += 1
    print(f"{arrIdx} - {arr[arrIdx]} , {seqIdx}")
    arrIdx += 1
  return seqIdx == len(sequence)

def validateSubsequenceFor(sequence, arr):
  seqIdx = 0
  for value in arr:
    if seqIdx == len(sequence):
      break
    if sequence[seqIdx] == value:
      seqIdx += 1
  return seqIdx == len(sequence)

if __name__ == "__main__":
  val = validateSubsequence([1,-1,4],[0,1,4,-1,4,5])
  print(val)
