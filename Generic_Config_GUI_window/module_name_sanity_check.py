import re

def is_valid_string(input_string):
    # Regular expression pattern
    # ^         : Start of the string
    # [a-zA-Z_] : Must start with an alphabet or '_'
    # \w*       : Followed by any number of word characters (alphanumeric characters plus '_')
    # $         : End of the string
    pattern = r'^[a-zA-Z_]\w*$'
    
    # Match the input string with the pattern
    if re.match(pattern, input_string):
        return True
    else:
        return False