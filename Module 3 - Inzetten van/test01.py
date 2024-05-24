#Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

#Examples:
def solution(string, ending):
    return string.endswith(ending)

print(solution('abc', 'bc'))# returns true
print(solution('abc', 'd'))# returns false