def jobsequencer(arr):
  maxdeadline = float("-inf")
  for idx in range(len(arr)):
    if arr[idx][1] > maxdeadline:
      maxdeadline = arr[idx][1]
  
  outputjobarr = [None]*maxdeadline
  maxp = float("-inf")
  jobsfilled = 0
  jobsprocessed = {}

  while jobsfilled < maxdeadline:
    for idx in range(len(arr)):
      if arr[idx][2] > maxp and arr[idx][0] not in jobsprocessed:
        maxp = arr[idx][2]
        maxj = arr[idx][0]
        maxd = arr[idx][1]
    maxp = float("-inf")
    jobsprocessed[maxj] = True

    for idx2 in range(maxd-1,-1,-1):
      if outputjobarr[idx2] == None:
        outputjobarr[idx2] = maxj
        jobsfilled += 1
        break
  return outputjobarr
