def solution(s):
    
    maxVal = 0
    
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            tmpStr = s[i:j] #i~j-1까지 슬라이싱 되므로 len(s)부터 시작, range역시 i+1까지 작동하므로 i로 설정
            if (tmpStr == tmpStr[::-1]):
                maxVal = max(maxVal, len(tmpStr))
    
    return maxVal