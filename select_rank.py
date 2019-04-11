
def selectRank(rank, L, fromIndex, toIndex):
    """
    Returns the pair (value, index) of the element in
    L[fromIndex : toIndex] with the desired rank.
    """
    if toIndex == fromIndex + 1:
        return (L[fromIndex], fromIndex)

    pivot, pivotIndex = selectPivot(L, fromIndex, toIndex) 
    pivotIndex = partition(pivotIndex, L, fromIndex, toIndex)
    pivotRank = pivotIndex - fromIndex + 1

    if rank < pivotRank:
        return selectRank(rank, L, fromIndex, pivotIndex) 

    if rank > pivotRank:
        return selectRank(rank - pivotRank, L, pivotIndex+1, toIndex)
    
    return (pivot, pivotIndex)


def selectPivot(L, fromIndex, toIndex):
    """
    Divides L[fromIndex : toIndex] into chunks of five elements,
    computes the median of each chunk, and applies selectRank to
    compute the median of medians. The result is a pivot that
    partitions the given segment approximately around its median.
    """
    mediansFrontier = fromIndex
    for fromChunkIndex in range(fromIndex, toIndex, 5):
        toChunkIndex = min(fromChunkIndex + 5, toIndex)
        moveMedianToFront(mediansFrontier, L, fromChunkIndex, toChunkIndex)
        mediansFrontier += 1

    medianOfMedians = (mediansFrontier - fromIndex + 1)//2
    return selectRank(medianOfMedians, L, fromIndex, mediansFrontier)


def moveMedianToFront(position, L, fromIndex, toIndex):
    """
    Computes the median of L[fromIndex : toIndex] and moves it 
    to the specified position.
    """
    insertionSort(L, fromIndex, toIndex)
    medianIndex = (fromIndex + toIndex - 1)//2
    L[medianIndex], L[position] = L[position], L[medianIndex]
    

def insertionSort(L, fromIndex, toIndex):
    """
    Sorts L[fromIndex : toIndex].
    """
    for valueIndex in range(fromIndex+1, toIndex):
        value = L[valueIndex]
        index = valueIndex-1
        while index >= fromIndex and L[index] > value:
            L[index+1] = L[index]
            index -=  1
        L[index+1] = value 


def partition(pivotIndex, L, fromIndex, toIndex):
    """
    Partitions L[fromIndex : toIndex] around the given pivot.
    """
    L[fromIndex], L[pivotIndex] = L[pivotIndex], L[fromIndex]

    pivot = L[fromIndex]
    pivotIndex = fromIndex
    for index in range(fromIndex+1, toIndex):
        if L[index] < pivot:
            pivotIndex += 1
            L[pivotIndex], L[index] = L[index], L[pivotIndex]

    L[fromIndex], L[pivotIndex] = L[pivotIndex], pivot

    return pivotIndex

