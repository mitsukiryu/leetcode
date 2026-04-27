def isValid(s):
    if not s:
        return False
    char_list = list(s)
    queue = []
    queue.append(char_list.pop(0))
    valid = 1
    for p in char_list:
        if p == ")" or p == "]" or p == "}":
            if not queue:
                valid = 0
                break
            if p == ")" and queue.pop() != "(":
                valid = 0
                break
            elif p == "]" and queue.pop() != "[":
                valid = 0
                break
            elif p == "}" and queue.pop() != "{":
                valid = 0
                break
        else:
            queue.append(p)
    if valid and not queue:
        return True
    else:
        return False


print(isValid("()"))
