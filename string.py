# 58
def lengthOfLastWord(self, s: str) -> int:
    s = s.strip()
    c = 0
    if s[len(s)-1] == ' ':
        return 0
    elif " " not in s:
        return len(s)

    for i in range(len(s)-1, 0, -1):
        if s[i] != ' ':
            c += 1
        else:
            return c


# 14
def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ''
    else:
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i)) == 1:
                prefix += i[0]
            else:
                break
        return prefix
