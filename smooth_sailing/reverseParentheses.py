def reverseParentheses(s):
    chars = list(s)
    open_paren_indexes = []
    for i, c in enumerate(chars):
        if c == '(':
            open_paren_indexes.append(i)
        elif c == ')':
            j = open_paren_indexes.pop()
            chars[j:i] = chars[i:j:-1]
    return ''.join(c for c in chars if c not in '()')
