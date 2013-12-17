from ..stringreverse.reverse_string import reverse_string


def is_palindrome(string):
    return string == reverse_string(string)
