def countBits(self, n: int) -> List[int]:
    def cnt(v):
        c = ((v & 0xfff) * 0x1001001001001 & 0x84210842108421) % 0x1f
        c += (((v & 0xfff000) >> 12) * 0x1001001001001 & 0x84210842108421) % 0x1f
        c += ((v >> 24) * 0x1001001001001 & 0x84210842108421) % 0x1f
        return c
    ans = [] 
    for i in range(n+1):
        ans.append(cnt(i))
    return ans
