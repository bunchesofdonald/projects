#!/usr/bin/env python


def reverse_string(string):
    result = []
    for i in range(len(string) - 1, -1, -1):
        result.append(string[i])

    return ''.join(result)
