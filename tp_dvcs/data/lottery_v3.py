#!/usr/bin/env python
""" Example program for JDEV Mercurial tutorial """
from optparse import OptionParser

def calculate_result(white_balls, power_ball):
    """ Computation is lauched here """
    
    for ball in white_balls:
        if ball < 1 or ball > 59:
            return -1

    if power_ball < 1 or power_ball > 39:
        return -1

    return 0

def main():
    """ Program used to compute the integer percent of chance
    of winning at the lottery.
    Five white balls and a power ball are drawn"""
    
    usage = "Usage: %prog power_ball (5 white balls)"
    parser = OptionParser(usage)

    (_, args) = parser.parse_args()
    
    if len(args) != 6:
        parser.error("incorrect number of arguments")

    power_ball = int(args[0])

    white_balls = [int(arg) for arg in args[1:]]

    result = calculate_result(white_balls, power_ball)

    print "White balls : %s" % white_balls
    print "Chance ball : %s" % power_ball

    print "%d percent chance of winning" % result

    return 0

if __name__ == "__main__":
    main()
