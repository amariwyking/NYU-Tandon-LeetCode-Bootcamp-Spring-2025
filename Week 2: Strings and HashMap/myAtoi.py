def myAtoi(self, s: str) -> int:
        # clip leading whitespace
        s = s.lstrip()

        if not s:
            return 0

        ptr = 0

        factor = 1

        if s[ptr] == "-":
            factor = -1
            ptr = 1
        elif s[ptr] == "+":
            ptr = 1

        # check that there are characters after the sign
        if not s[ptr:]:
            return 0

        if ord(s[ptr]) < ord("0") or ord(s[ptr]) > ord("9"):
            return 0

        # initialize construction
        integer = ""

        # construct integer
        for c in s[ptr:]:
            if ord(c) < ord("0") or ord(c) > ord("9"):
                break

            integer += c     

        # otherwise check if we need to round
        integer = int(integer) * factor

        if integer < 0:
            return max(-(2**31), integer)
        else:
            return min(2**31 - 1, integer)