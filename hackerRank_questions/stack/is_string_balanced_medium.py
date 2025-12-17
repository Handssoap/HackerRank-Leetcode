def isBalanced(s):
    stack = []
    # characters to check
    starting = ['{', '[', '(']
    for char in s:
        # if starting bracket, append to list
        if char in starting:
            stack.append(char)
            continue
        # if there are no opening brackets, and current is closing, return no
        elif len(stack) == 0:
            return 'NO'
        elif stack[len(stack) - 1] == '{' and char == '}':
            stack.pop()
        elif stack[len(stack) - 1] == '(' and char == ')':
            stack.pop()
        elif stack[len(stack) - 1] == '[' and char == ']':
            stack.pop()
        else:
            return 'NO'
    # if stack is not empty at end of closing all brackets, return no
    if len(stack) > 0:
        return 'NO'
    else:
        return 'YES'