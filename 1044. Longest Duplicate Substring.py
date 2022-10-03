def longestDupSubstring(self, s: str) -> str:
    def serch(n):
        h = set()
        l = 0
        while n+l<len(s):
            p = s[l:n+l+1]
            if p in h:
                return p
            h.add(p)
            l+=1
        return False

    l,r = 0,len(s)
    while l<=r:
        mid = (l+r)//2
        k = serch(mid)
        if k:
            l = mid+1
        else:
            r = mid-1

    return serch(r) if l else ''
