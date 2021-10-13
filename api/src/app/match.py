def match(pattern, string):
    
    if pattern == string == '':
        return True

    #two pointers, one for pattern, one for string
    pointer_p = 0
    pointer_s = 0
  
    while (pointer_p < len(pattern)):

        #if * in pattern, keep counting pointer_s until the pattern stops repeating
        if (pattern[pointer_p] == '*'):
            p_char_after = pattern[pointer_p+1]
            if(p_char_after !=string[pointer_s]):
                repeat_char = string[pointer_s]
                while (string[pointer_s] == repeat_char and pointer_s < len(string)):
                    pointer_s+=1
            pointer_p+=1
            
        #if !, skip a character in both
        if(pattern[pointer_p] == '!'):
            pointer_s += 1
            pointer_p += 1
            
        if(pattern[pointer_p] == string[pointer_s]):
            pointer_p += 1
            pointer_s += 1

    if (pointer_p == len(pattern) and pointer_s == len(string)):
        print('True')
        return True

    print('False')
    return False
    