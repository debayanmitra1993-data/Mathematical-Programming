def combinations(arr, k):
    if k <= len(arr):
        if k == 1:
            combs = []
            for idx in range(len(arr)):
                combs.append([arr[idx]])
            return combs
        elif k > 1:
            combs = []
            for idx in range(len(arr)-k+1):
                curr_ele = arr[idx]
                remaining_arr = arr[idx+1:]
                combs_remaining_arr = combinations(remaining_arr,k-1)
                for comb in combs_remaining_arr:
                    combs.append([curr_ele] + comb)
            return combs
    else:
        return []
