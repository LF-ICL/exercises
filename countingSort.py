def countingSort(arr):
    countList = [0] * (100)
    for i in range(len(arr)):
        countList[arr[i]] += 1
    # return countList # Use this line if only the index list is required.
    output = []
    for i in range(len(countList)):
        # if countList[i] > 0:
        output+=([i]*countList[i])
    return output # Use this line if the sorted list is required.
