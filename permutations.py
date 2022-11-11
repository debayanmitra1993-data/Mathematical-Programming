# Code snippet to generate all permutations of an array using recursion
# example [1,2,3] -> 3! permutations
# all permutations of [1,2,3] -> [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

def permutations(arr):
  if len(arr) == 2:
    return [[arr[0],arr[1]],[arr[1],arr[0]]]
  elif len(arr) > 2:
    perms = []
    for idx in range(len(arr)):
      curr_ele = arr[idx]
      remaining_arr = arr[:idx] + arr[idx + 1:]
      perms_remaining_arr = permutations(remaining_arr)
      for perm in perms_remaining_arr:
        perms.append([curr_ele] + perm)
    return perms
