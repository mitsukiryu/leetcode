def lengthOfLongestSubString(s):
    max_s = ""
    sub_s = ""
    p1 = -1
    for i in range(len(s)):
        for j in range(p1 + 1, i):
            if s[i] == s[j]:
                print("dulicate found in %d" % (j))
                sub_s = s[p1 + 1 : i]
                p1 = j
                if len(max_s) < len(sub_s):
                    max_s = sub_s
                break

        if i >= len(s) - 1:
            sub_s = s[p1 + 1 :]
            if len(max_s) < len(sub_s):
                max_s = sub_s
            break

        if p1 == -1:
            return s
        else:
            return max_s


print(lengthOfLongestSubString("cdd"))
