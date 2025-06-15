# 2[abc]3[cd]e

from collections import deque

def decodeString(s: str) -> str:
    # initialize a stack
    stack = deque()

    # iterate through every character in the string
    for i in range(len(s)):
        # if the character isn't a closing bracket
        if s[i] != "]":
            # add it to the top of the stack
            stack.append(s[i])
        else:
            # otherwise, we need to determine the contents of this bracket pair
            substr = ""
            
            # we are guaranteed to hit an opening bracket before reaching a digit or the bottom of the stack
            while stack[-1] != "[":
                # since we are reading the characters in reverse order we need to add to the start of the substring
                substr = stack.pop() + substr

            # Pop the opening parenthese
            stack.pop()

            # once the substring is constructed we are ready to determine how many times it should be repeated
            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k

            stack.append(int(k) * substr)

    return "".join(stack)