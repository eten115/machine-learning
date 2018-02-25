# coding=utf-8
#

import math


def calc_sqrt_3():

    f_x = lambda x: float(math.pow(x, 2) - 3)
    f_d_x = lambda x: float(2 * x)

    h_x = lambda x: x - f_x(x)/f_d_x(x)

    # init (2, 1)

    xn = 1
    xn1 = 2
    round_count = 0
    while True:
        round_count += 1
        print "round: %f, xn: %f" % (round_count, xn)

        xn1 = h_x(xn)
        if abs(xn - xn1) < 0.000000000001:
            print xn1
            break
        else:
            xn = xn1

        pass

    pass


if __name__ == '__main__':
    print "hello world"
    calc_sqrt_3()

