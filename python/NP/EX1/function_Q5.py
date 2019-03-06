import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def perfect_square(n):
    return round(n**(1/2))


test(perfect_square(15) == 4)
test(perfect_square(31) == 6)
test(perfect_square(41) == 6)
test(perfect_square(99) == 10)
