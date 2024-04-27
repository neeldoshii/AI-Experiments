import math
# root node starts with max so it takes true at start
# min --> false
# max --> true
def minimax (curDepth, nodeIndex,
maxTurn, scores,
targetDepth):

  # base case : targetDepth reached
  if (curDepth == targetDepth):
      return scores[nodeIndex]
  # returns the max value from the left & right node from the true and calls false (min) recursively
  if (maxTurn):
      return max(minimax(curDepth + 1, nodeIndex * 2,
      False, scores, targetDepth),
      minimax(curDepth + 1, nodeIndex * 2 + 1,
      False, scores, targetDepth))
  
  # returns the min value from the left & right node from the false and calls true (max) recursively
  else:
      return min(minimax(curDepth + 1, nodeIndex * 2,
      True, scores, targetDepth),
      minimax(curDepth + 1, nodeIndex * 2 + 1,
      True, scores, targetDepth))
  

scores = [3, 5, 2, 9, 12, 5, 23, 23]
treeDepth = math.log(len(scores), 2) #8log2 = 2^3 = 8 ---> depth is 3
print("The optimal value is : ", end = "")
print(minimax(0, 0, True, scores, treeDepth))