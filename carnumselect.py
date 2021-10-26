import sys
import math
import argparse
from termcolor import colored

GoodNumSum = [1,3,5,6,7,8,11,13,15,16,17,18,21,23,24,25,29,31,32,33,35]
GoodNumRemainder = [1,3,5,6,7,8,11,13,15,16,17,18,21,23,24,25,28,30,31,32,34,36,40,44,46,47,51,56,62,64,66,67,72,80]

def calMethod(carnum, method, verbose):
    rt = 0

    if method == 'remainder':
        print("method 81 cal starting...") if verbose else None

        rt1 = int(carnum) / 80
        print("%s" % rt1) if verbose else None 

        rt2 = math.floor(rt1*1) / 1.0
        print("%s" % rt2) if verbose else None

        rt3 = 80*(math.floor((rt1 - rt2)*10000) / 10000.0)
        print("%s" % rt3) if verbose else None

        rt = int(math.ceil(rt3*1) / 1.0)
    elif method == 'sum':
        carnumstr = str(carnum)
        rt = int(carnumstr[0])+int(carnumstr[1])+int(carnumstr[2])+int(carnumstr[3])

    return rt

def formateResultStr(resultNum, calMethod):
    goodNums = None
    
    if calMethod == 'remainder':
        goodNums = GoodNumRemainder
    elif calMethod == 'sum':
        goodNums = GoodNumSum
    
    if resultNum in goodNums:
        carnumstrs = ['GOOD', 'green']
    else:
        carnumstrs = ['BAD', 'red']

    return carnumstrs

def main():
    parser =argparse.ArgumentParser()#(description='usage: carnumselect.py --carnum [Car Plate Number] [OPTIONS]')
    parser.add_argument('-cn', '--carnum', nargs=1, type=str, help='4 digit car plate number to be calculated')
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help='display the calculation process')
    args = parser.parse_args()
    
    try:
        rt = calMethod(args.carnum[0], 'remainder', args.verbose)
        rstrs = formateResultStr(rt, 'remainder')
        print("The calculated car plate number by Remainder method is %s --> %s" % (rt, colored(rstrs[0], rstrs[1])))
        
        rt = calMethod(args.carnum[0], 'sum', args.verbose)
        rstrs = formateResultStr(rt, 'sum')
        print("The calculated car plate number by Sum method is %s --> %s" % (rt, colored(rstrs[0], rstrs[1])))
    except:
        print('run python3 carnumselect.py --help for more information')
       
    
if __name__ == '__main__':
    main()