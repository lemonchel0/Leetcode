def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
    tokens.sort()
    if not tokens:
        return 0
    if power < tokens[0]:
        return 0
    l,r = 0, len(tokens)-1
    score = 0
    ans = 0
    while l < r:
        if power >= tokens[l]:
            score+=1
            power-=tokens[l]
            l+=1
        else:
            score-=1
            power+=tokens[r]
            r-=1
        if score < 0:
            break
        ans = max(score,ans)
    if l == r and power >=tokens[l]:
        ans=max(score+1,ans)
    return ans
            
