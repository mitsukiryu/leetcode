def myAtoi(s):
    result = ""
    for p in range(len(s)):
        if s == "":
            return 0
        if s[p] == " ":
            continue
        elif s[p].isdigit() or s[p] == "+" or s[p] == "-":
            if s[p] == "+":
                p += 1
            elif s[p] == "-":
                result += "-"
                p += 1
            elif not s[p].isdigit():
                return 0
            for i in range(p, len(s)):
                if s[i] != "0" and s[i].isdigit():
                    break
                elif s[i] == "0" and i == len(s) - 1:
                    return 0
                elif not s[i].isdigit():
                    return 0
                p += 1
            s = s[p:]
            print(s)
            for p2 in s:
                if p2.isdigit():
                    result += p2
                else:
                    break
            result = int(result) if result and result != "-" else 0
            if result > 2147483647:
                return 2147483647
            elif result < -2147483648:
                return -2147483648
            else:
                return result
        else:
            return 0
    return 0


print(myAtoi(" -042"))
