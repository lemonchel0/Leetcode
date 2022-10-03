def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
    a = collections.Counter(arr)
    b = list(a.values())
    b.sort()
    s,i = 0,0
    while s<k:
        s+=b[i]
        i+=1
    if s == k:
        return len(b) - i
    return len(b) - i + 1
