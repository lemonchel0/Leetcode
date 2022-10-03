def minCost(self, colors: str, t: List[int]) -> int:
    prev = colors[0]
    pos = 0
    ans =0
    for i in range(1,len(colors)):
        if prev == colors[i]:
            continue
        ans+=sum(t[pos:i])-max(t[pos:i])
        pos = i
        prev = colors[i]
    ans+=sum(t[pos:len(colors)])-max(t[pos:len(colors)])
    return ans
