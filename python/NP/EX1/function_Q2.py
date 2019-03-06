import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def sum_of_digit_square(args):
    args_abs = abs(args) == args and args or abs(args)
    return sum(list(map(lambda v: int(v)**2, list(str(args_abs)))))


test(sum_of_digit_square(789) == 7 ** 2 + 8 ** 2 + 9 ** 2)
test(sum_of_digit_square(-123) == 1 ** 2 + 2 ** 2 + 3 ** 2)

