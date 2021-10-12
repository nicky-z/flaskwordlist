

def match(pattern, string):
    """
    Pattern Matching

    Take an input `pattern` and an input `string` and determine if they match. Pattern may use
    the following special characters:

      * = match against 0 or more arbitrary characters
      ! = match a single arbitrary character

    """

    if pattern == string == '':
        return True

    return False
