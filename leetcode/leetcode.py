def isValid(ss):
    stack = []
    dict_ = {')': '(', '}': '{', ']': '['}
    for s in ss:
        if s in dict_:
            top_element = stack.pop() if stack else '#'
            print(top_element)
            if dict_[s] != top_element:
                return False
        else:
            stack.append(s)
    return not stack


def longestValidParentheses(s):
    if len(s)== " ":
        return 0
    else:
        dict_ = {')': '('}
        stack = []
        count = 0
        res = [0]
        for char in s:
            if char in dict_:
                top_element = stack.pop() if stack else '#'
                if dict_[char] == top_element:
                    count = count + 2
                    print(type(count), count)
                    res.append(count)
                    print(res)
            else:
                stack.append(char)
                if len(stack) > 1:
                    count = 0
        return max(res)


def main():
    str_ = input("input a str:")
    print(longestValidParentheses(str_))

if __name__=='__main__':
    main()




