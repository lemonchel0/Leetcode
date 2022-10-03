def findOriginalArray(self, c: List[int]) -> List[int]:
    if len(c)%2:
        return []
    ans = []
    a = collections.Counter(c)
    c = list(a.keys())
    c.sort()
    if 0 in a:
        if a[0]%2:
            return []
        ans+=[0]*(a[0]//2)
        a[0]=0
    for i in c:
        if a[i] == 0:
            continue
        if 2*i in a and a[i]<=a[2*i]:
            ans+=[i]*a[i]
            a[2*i] -= a[i]
        else:
            return []
    return ans
