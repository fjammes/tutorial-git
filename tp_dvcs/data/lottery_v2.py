""" Example program for JDEV Mercurial tutorial """
#!/usr/bin/env python
from optparse import OptionParser

def calculate_result(white_balls, power_ball):
    """ Computation is lauched here """
    return 0

def main():
    """ Program used to compute the integer percent of chance
    of winning at the lottery.
    Five white balls and a power ball are drawn"""
    
    usage = "Usage: %prog (5 white balls) power_ball"
    parser = OptionParser(usage)

    (_, args) = parser.parse_args()
    
    if len(args) != 6:
        parser.error("incorrect number of arguments")

    power_ball = int(args[5])

    white_balls = [int(arg) for arg in args[:5]]

    result = calculate_result(white_balls, power_ball)

    print "White balls : %s" % white_balls
    print "Chance ball : %s" % power_ball

    print "%d percent chance of winning" % result

    return 0

if __name__ == "__main__":
    main()
