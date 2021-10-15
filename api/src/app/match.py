def match(pattern, string):

    #base cases: if reached end of one & not the other : return False
    # if reached end of both : return True
    if not pattern: 
        return not string

    if not string:
        return not pattern
    #if the first character is a normal letter
    if pattern[0] not in ["*", "!"]: 
        return pattern[0] == string[0] and match(pattern[1:], string[1:])
    #if the first letter is a special char
    #skip 1 letter if it's '!'
    #continue looping til the end if it's * 
    start = 0 if pattern[0] == "*" else 1
    for i in range(start, len(string)): 
        if match(pattern[1:], string[i:]):
            print('True')
            return True

    print('False')
    return False
