import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def even_filter(l):
    arr = list()
    for i in l:
        i % 2 == 0 and arr.append(i) or ''
    return arr


test(even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 4, 6, 8])
test(even_filter([1, 3, 5, 7, 9]) == [])
