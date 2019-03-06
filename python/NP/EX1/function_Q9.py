import sys
import math


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def my_gcd(a, b):
    a = abs(a)
    b = abs(b)
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a


test(my_gcd(12, 16) == math.gcd(12, 16))
test(my_gcd(16, 12) == math.gcd(16, 12))
test(my_gcd(9, 6) == math.gcd(9, 6))
test(my_gcd(-12, -38) == math.gcd(-12, -38))
