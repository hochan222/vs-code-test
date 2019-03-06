import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def star_pattern(n):
    star = ''
    star += '```python\n'
    for i in range(1, n+1):
        star += '*'*i + '\n'
    for i in range(1, n):
        star += '*'*(n-i) + '\n'
    star += '```'
    return print(star)


star_pattern(5)
star_pattern(6)
