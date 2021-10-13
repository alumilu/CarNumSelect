import sys
import math
import argparse

GoodNumSum = [1,3,5,6,7,8,11,13,15,16,17,18,21,23,24,25,29,31,32,33,35]
GoodNum81 = [1,3,5,6,7,8,11,13,15,16,17,18,21,23,24,25,28,30,31,32,34,36,40,44,46,47,51,56,62,64,66,67,72,80]

def calMethod81(carnum, verbose):
    print("method 81 cal starting...") if verbose else None

    rt = int(carnum) / 80
    print("%s" % rt) if verbose else None 

    rt2 = math.floor(rt*1) / 1.0
    print("%s" % rt2) if verbose else None

    rt3 = 80*(math.floor((rt - rt2)*10000) / 10000.0)
    print("%s" % rt3) if verbose else None

    return int(math.ceil(rt3*1) / 1.0)

def calMethodSum(carnum, verbose):
    carnumstr = str(carnum)
    return int(carnumstr[0])+int(carnumstr[1])+int(carnumstr[2])+int(carnumstr[3])

def main():
    parser =argparse.ArgumentParser(description='usage: carnumselect.py [-h] -cn[--carnum] carnum [-v][--verbose]')
    parser.add_argument('-cn', '--carnum', nargs=1, type=str, help='4 digit car number to be calculated')
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help='display car number calculation process')
    args = parser.parse_args()
    
    try:
        rt = calMethod81(args.carnum[0], args.verbose)
        carnumstr = 'Good' if int(rt) in GoodNum81 else 'Bad'
        print("The calculated car number by 81 method is %s --> %s" % (rt, carnumstr))

        rt = calMethodSum(args.carnum[0], args.verbose)
        carnumstr = 'Good' if int(rt) in GoodNumSum else 'Bad'
        print("The calculated car number by 4-digit-sum method is %s --> %s" % (rt, carnumstr))
    except:
        print('carnumselect.py -h to see the usage')
    
if __name__ == '__main__':
    main()