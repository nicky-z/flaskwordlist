def match(pattern, text):
    if not pattern:
        return not text
    if not text:
        return pattern in ["*", ""]
    if pattern[0] not in ["*", "!"]: 
        return pattern[0] == text[0] and match(pattern[1:], text[1:])
    start = 0 if pattern[0] == "*" else 1
    for i in range(start, len(text)):
        if match(pattern[1:], text[i:]):
            print('True')
            return True
    print('False')
    return False