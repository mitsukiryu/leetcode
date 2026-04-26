def longestCommonPrefix(strs):
    LCP = strs.pop(0)
    for i in strs:
        print(i)
        for c in range(len(LCP)):
            print(i[c])
            print(LCP[c])
            if i[c] != LCP[c]:
                LCP = LCP[:c]
                break
    return LCP


print(longestCommonPrefix(["flower", "flow", "flight"]))
